#!/usr/bin/env python

"""
Description:
Given a dictionary (may be nested), flatten it keeping the parent key references intact.

Sample Input:

{
  'Key1': '1',
  'Key2': {
    'a' : '2',
    'b' : '3',
    'c' : {
      'd' : '3',
      'e' : '1'
      }
    }
}

Sample Output:

{
  'Key1': '1',
  'Key2.a': '2',
  'Key2.b' : '3',
  'Key2.c.d' : '3',
  'Key2.c.e' : '1'
}

"""
__author__ = "vivek"


def flatten_dict_rec(in_dict, prefix=''):
    """
    Given a dictionary, flatten it recurvisely.
    :param in_dict (dict): input dictionary
    :param prefix (str) [optional] [default=' ']: the prefix for keys of current dictionary.

    :return (dict): flatten dictionary.
    """

    out_dict = dict()

    for key, value in in_dict.items():

        if isinstance(value, dict):
            # if current key value pair is a nested dictionary,
            # call the flatten_dict_rec with current value (dict), and updated prefix.
            # unpack the result dictionary, and merge it with the output dictionary.

            out_dict = dict(out_dict, **flatten_dict_rec(value, prefix + key + '.'))

        else:
            # if current value is a string/normal value,
            # add it to the output dictionary directly with proper key.

            out_dict[prefix + key] = value

    return out_dict 


def flatten_dict_iter(in_dict, prefix=''):
    """
    Given a dictionary, flatten it iteratively.
    :param in_dict (dict): input dictionary
    :param prefix (str) [optional] [default=' ']: the prefix for keys of current dictionary.

    :return (dict): flatten dictionary.
    """

    out_dict = dict()
    stack = list()

    stack.append([in_dict, prefix])

    while stack:
        top_item = stack.pop()
        curr_dict, prefix = top_item[0], top_item[1]

        for key, value in curr_dict.items():

            if isinstance(value, dict):
                # if current key value pair is a nested dictionary,
                # add the current value (dict), and updated prefix pair to the stack.

                stack.append([value, prefix + key + '.'])

            else:
                # if current value is a string/normal value,
                # add it to the output dictionary directly with proper key.

                out_dict[prefix + key] = value

    return out_dict


def main():

    in_dict = {
               'Key1': '1',
               'Key2': {
                        'a' : '2',
                        'b' : '3',
                        'c' : {
                               'd' : '3',
                               'e' : '1'
                              }
                       }
              }
    print("\nOriginal dictionary: ")
    print(in_dict)

    print("\nRecursive flatten: ")
    print(flatten_dict_rec(in_dict))

    print("\nIterative flatten: ")
    print(flatten_dict_iter(in_dict))


if __name__ == "__main__":
    main()
