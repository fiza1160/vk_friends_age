import requests


def calc_age(uid):
    token = '8abcb1528abcb1528abcb152408ad43e5388abc8abcb152d6e13d15574a6a3ca2d54608'

    id = get_id(uid, token)
    friends = get_friends(id, token)
    counted_age_of_friends = count_friends_of_same_age(friends)
    result = format_data_for_output(counted_age_of_friends)

    return result


def get_id(uid, token):
    request = 'https://api.vk.com/method/users.get?v=5.71&access_token={token}&user_ids={uid}'.format(
        token=token, uid=uid
    )
    r = requests.get(request)
    response = r.json()
    if 'error' in response:
        raise ValueError

    id = r.json()["response"][0]["id"]

    return id


def get_friends(id, token):
    request = 'https://api.vk.com/method/friends.get?v=5.71&access_token={token}&user_id={id}&fields=bdate'.format(
        token=token, id=id
    )
    r = requests.get(request)
    response = r.json()

    if 'error' in response:
        raise ValueError
    friends = response["response"]["items"]
    return friends


def count_friends_of_same_age(friends):
    age_dict = {}

    for friend in friends:
        if 'bdate' in friend:
            year = get_year(friend['bdate'])
            if year is not None:
                age = 2019 - year
                if age not in age_dict:
                    age_dict[age] = 0
                age_dict[age] += 1

    return age_dict


def get_year(date):
    data_date = date.split(".")
    if len(data_date) < 3:
        return None
    return int(data_date[2])


def format_data_for_output(age_dict):
    data_for_output = []

    for age, count in age_dict.items():
        data_for_output.append((age, count))

    data_for_output.sort(key=lambda x: (-x[1], x[0]))

    return data_for_output


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
