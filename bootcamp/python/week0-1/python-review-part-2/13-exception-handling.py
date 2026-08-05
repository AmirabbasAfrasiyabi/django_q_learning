def main():
    try:
        n = int(input())
        if n < 0:
            raise Exception('The input should not be negative')
        return n * 2
    except Exception as e:
        return e
    finally:
        print('Finally')

print(main())
