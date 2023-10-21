def main():

    original_str = 'Python Programming'
    ##################################################
    # Comlete your code here
    ##################################################

    split_str = original_str.split(" ")

    sub1 = split_str[0]
    sub2 = split_str[1]
    merged_str = sub1 + " " + sub2
    print(sub2)
    print(sub1)
    print(merged_str)

    #########################################
    # Do not delete the return statement
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
