import pandas as pd


def orders_order_reviews(data):
    """
    Input: data dictionary with all datasets as values.
    Output: merged and cleaned dataset of orders and order_reviews
    """

    orders = data["orders"]
    order_reviews = data["order_reviews"]

    ## For orders with more than one review I set the latest review as the right one
    # first create a df with all orders with more than one review
    #  this df is sorted by order_id and review_creation_date with
    #  the lastest review being on top
    temp = pd.concat(g for _, g in order_reviews.groupby("order_id") if len(g) > 1)\
                            .sort_values(by = ["order_id", "review_creation_date"],
                            ascending=[True, False])["order_id"]

    # drop returns true for the second or third occurrence of an order_id
    drop = temp.duplicated(keep = "first")
    # the indeces of the second and third order_ids are saved
    drop_index = temp[drop].index
    # the indeces of the second and third order_ids are filtered out
    orders = orders[~ orders.index.isin(drop_index)]

    # merge orders and order_reviews
    orders_order_reviews = orders.merge(order_reviews, how = "inner", on = "order_id")


    # drop orders with no reviews
    orders_order_reviews.dropna(subset=["review_id"], inplace=True)
