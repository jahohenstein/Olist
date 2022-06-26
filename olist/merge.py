import pandas as pd


def orders_order_reviews(data):
    """
    Input: data dictionary with all datasets as values.
    Output: merged and cleaned dataset of orders and order_reviews
    """

    orders = data["orders"]
    order_reviews = data["order_reviews"]


    # merge orders and order_reviews
    orders_order_reviews = orders.merge(order_reviews, how = "inner", on = "order_id")


    # drop orders with no reviews
    orders_order_reviews.dropna(subset=["review_id"], inplace=True)
