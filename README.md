# Hotel Cancellation Predictor

**Author**: [Matthew Duncan](mailto:mduncan0923@gmail.com)

### This is currently a work in progress. For more details on the current status, please check out my [notebook](./Hotel_Cancellation_Notebook.ipynb).

![hotel_intro](./Images/Hotel_intro.jpg)

## Overview/Business Understanding
Hotels are often plagued with last minutes cancellations as people's plans change, schedules conflict, or if a better price was found elsewhere. Research from Avvio.com [shows](https://www.avvio.com/2022-cancellation-rate-trends/) that revenue lost due to  hotel room cancellations increased 33% from 2019 to 2022.

The goal of this analysis is to use past information about a particular guest (i.e. have they cancelled in the past?), along with information about their stay and requests (i.e. room type, length of stay), to predict whether the guest is likely to cancel their reservation or not show up at all. 

### Cost of Errors
Being able to predict whether a guest is likely to cancel would be a huge benefit to the hotel. Having an idea of potential cancellations would allow management to better plan for staffing, food budgets, and other commodities that depend on guest levels. 

Precision is important in this analysis as we want to minimize the number of false positives (when the model predicts that a guest will cancel but the guest does not actually cancel) to ensure a high level of customer service for guests. Incorrectly predicting that a guest will cancel when they do not could cause issues with potential overbooking, lack of supplies or staff, or delays in preparing the guests room.

![Hotel_img2](./Images/hotel2.jpg)

## Understanding the Data

The dataset contains 36,275 data entries with no null values in the dataset. There are a total of 19 columns including a unique identifier column `Booking_ID` and the target column `booking_status`. 

Dates range from July 1, 2017 to December 31, 2018. There was a discrepency in the data that had a February 29 date for the year 2018. Since 2018 was not a leap year, the dates have been adjusted to read as the 28th.

The dataset features are primarily numerical with three categorical columns: `type_of_meal_plan`, `room_type_reserved`, `market_segment_type`.


Notable missing features:
- Hotel rating/stars
- Hotel Location
- Size of hotel/number of rooms the hotel has


The average hotel stay is for two adult guests with no children for a long weekend (1 week night and 2 weekend nights) booked about 3 months in advance. The average hotel room price is about $103.

In this repo, I have included the `hab_functions.py` with custom functions needed to run this notebook. I have also the `environment.yml` to ensure that you have the correct environment to run the notebook.

