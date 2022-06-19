# Olist
Analysis of the Kaggle Olist Dataset, with the focus on Visualization and Business Intelligence Analysis.

Work in Progress as of 15.6.2022

## Data

The dataset can be downloaded from Kaggle (https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download). The data was downloaded on 15.6.2022.

The dataset is divided into 9 CSV files, the structure of which is shown in the following image:

![image-20220615112558634](C:\Users\jakob\AppData\Roaming\Typora\typora-user-images\image-20220615112558634.png)



## Structure

### Data Analysis

#### Business Development

I will first focus on the question of how Olist's sales developed over time in terms of sales volume, turnover, customer satisfaction, variety of products, variety of sellers, regional distribution ...

##### Factors driving customer satisfaction

The next step will be to check for factors that influence customer satisfaction (i.e. review scores). The idea is to identify whether certain sellers are responsible for the majority of bad reviews, whether a late delivery annoys customers or whether some product categories are just of bad quality.

### Business implications

Starting from the results of our data analysis I will think of ways to increase Olist's income. Therefore I will assume that Olist gets a fixed fee from each seller for each month listed on Olist (listing fee) and a percentage share of each sold item (10 % of item price).

On the cost side, I will assume that Olist's IT costs increase with the square root of order volume. As a starting point, I will assume that the overall IT costs in the period observed were 1 Mil. BRL.

The question to be answered is whether an increase in customer satisfaction can increase Olist's income. Therefore I will make assumptions about the economical costs of a bad review.





### Further ideas for later implementation

- sales prediction
- text analysis to check for reasons for bad reviews
