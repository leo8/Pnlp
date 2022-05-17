# Data Generation

As it is not recommended by GitHub, rather than uploading the datasets we use in this project, we will provide an explanation of how to generate data.

1. First, open a web browser and go to https://data.stackexchange.com/stackoverflow/query/new

2. We generated two different datasets, QueryV1.csv and QueryV2.csv. The second contains more data that are a bit less relevant. Prompt the following SQL requests on Stack Exchange Data Explorer to generate the exact same datasets.

- To generate QueryV1.csv :

SELECT TOP 500000 Title, Body, Tags, Id, Score, ViewCount, FavoriteCount, AnswerCount
FROM Posts 
WHERE PostTypeId = 1 AND ViewCount > 10 AND FavoriteCount > 10
AND Score > 5 AND AnswerCount > 0 AND LEN(Tags) - LEN(REPLACE(Tags, '<','')) >= 5


- To generate QueryV2.csv :

SELECT TOP 500000 Title, Body, Tags, Id, Score, ViewCount, FavoriteCount, AnswerCount
FROM Posts 
WHERE PostTypeId = 1 AND ViewCount > 5 AND FavoriteCount > 5
AND Score > 5 AND AnswerCount > 0 AND LEN(Tags) - LEN(REPLACE(Tags, '<','')) >= 5

3. Finally, hit the 'Run query' button and manually download CSV files



