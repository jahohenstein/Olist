SELECT orders.order_id, order_reviews.review_score
	FROM orders
	INNER JOIN order_reviews ON (order_reviews.order_id = orders.order_id)
	WHERE order_reviews.review_score >= 4
	;