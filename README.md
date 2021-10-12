# Election Analysis Using Python

## Overview of Election Audit
The purpose of this project was to perform an audit of a congressional election. The objectives of the audit included:

1. Calculating the total number of votes cast.
2. Getting a complete list of candidates who recieved votes.
3. Calculating the total number of votes each candidate recieved. 
4. Calculating the percentage of votes each candidate won.
5. Determining the winner of the election based on popular vote.
6. Getting the voter turnout for each county
7. Calculating the percentage of votes from each county out of the total count
8. Calculating the county with the highest turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The election was held in a precint that encompassed Jefferson, Denver and Arapahoe counties.
- The county results were:
  - 10.5% of the vote and 38,855 number of votes came from Jefferson county
  - 82.8% of the vote and 306,055 number of votes came from Denver county
  - 6.7% of the vote and 24,801 number of votes came from Arapahoe county
- Denver county had the largest number of votes
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
 - The candidate results were: 
  - Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette recieved 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 number of votes.
 - The winner of the election was Diana DeGette, who recieved 73.8% of the vote and 272,892 number of votes.

 Below is a summary of the analysis that was transferred to a text file from python:
 ![election summary](https://github.com/mayamtims/Election-Analysis/blob/main/Resources/election_analysis.png)

 ## Election Audit Summary
 This script can be modified to obtain information about many different elections and elements of elections. With proper datasets provided, this script could be used as a template to find the winning candidate and county of any local election. The only information provided in the given dataset was ballot ID, county and candidate name for each voter. If further characteristics of each voter were provided in a dataset, this script could be used as a blueprint to obtain information beyond who won and how each county was represented. Many different demographics could be analyzed, such as the age, gender, race or socioeconomic class of voters in each county. 