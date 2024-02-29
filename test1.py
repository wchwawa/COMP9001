def main():

    # 新的数据结构：列表包含字典
    ticket_prices = [
        {"type": "adults", "price": 15},
        {"type": "children", "price": 6}
    ]

    visitor_count = {}
    tax_rate = 0.06
    total_price = 0

    # 遍历ticket_prices列表，每个元素是一个包含类型和价格的字典
    for visitor in ticket_prices:
        visitor_type = visitor["type"]
        prompt = f"Total {visitor_type}: "
        visitor_count[visitor_type] = get_int(prompt)
    
    print(visitor_count)

    # 计算每种访客类型的总价格
    for visitor in ticket_prices:
        visitor_type = visitor["type"]
        price = visitor["price"]
        count = visitor_count.get(visitor_type, 0)  # 使用.get()避免键不存在的错误
        category_total_price = price * count

        total_price += category_total_price

        print(f"The price for {visitor_type}: ${category_total_price:.2f}")

    # 计算并打印含税总价
    total_price_inc_tax = total_price * (1 + tax_rate)
    print(f"The price inclusive service tax: ${total_price_inc_tax:.2f}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please input an integer")


main()
