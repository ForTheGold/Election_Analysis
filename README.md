# Election_Analysis

## Overview

Tom, who works at the Board of Elections in Colorado, is tallying the votes for a congressional district.  The office has traditionally been doing this using Excel, which has been working, but he is looking for a way to automate the process using Python.

### Background

Tom is currently working on tallying the votes for of a specific congressional district in Colorado, and his office works with a variety of other congressional districts, elections with the senate as well as other local local elections.

### Collection Methods

The votes are collected through a variety of methods including mail in ballots, punch cards, and direct recording electronic machines (DREs).  The mail in ballots are hand counted, the punch cards machine counted and the DREs computer counted before being sent to the central office.

### Purpose

Tom has reached out to us looking to automate the process with a new system.  The organization has been tallying the votes in Excel thus far, but would like to use Python to build a program that can automate the process for this election and be applied to other elections as well.

The program is going to take into account all of the votes that have been recorded to produce a vote count report.  The report will be used to certify the race in this US congressional district.

## Election Audit Results

A program has been completed that takes in all of the data, counts up the total number of votes along with votes per a county and votes for each candidate.  The program prints a number of statistics that show the outcome of the election along with other additional information.

### Vote Statistics

* Total Votes: 369,711
* County Votes:
	* Jefferson: 10.5% (38,855)
	* Denver: 82.8% (306,055)
	* Arapahoe: 6.7% (24,801)
* Largest County Turnout: Denver
* Candidate Votes:
	* Charles Casper Stockham: 23.0% (85,213)
	* Diana DeGette: 73.8% (272,892)
	* Raymon Anthony Doane: 3.1% (11,606)
* Winner Statistics: 
	* Winner: Diana DeGette
	* Winning Vote Count: 272,892
	* Winning Percentage: 73.8%

![Election Results](https://github.com/ForTheGold/Election_Analysis/tree/main/Resources/election_results.png)

## Summary

This script has been used successfully for one election, but this is not the end of what can be done with it.  With minor modifications, this script can be used to tally the votes of a wide variety of different elections.  The simplest and easiest thing would be to use this script in another congressional district, but it could also be expanded to elections of senators or local politicians as well.

### Additional Congressional Districts

This script has been developed with expandability in mind.  The script does not use hard coded values for the names of the candidates running for congress or the names of the counties, but builds them based upon what is in the file.  A similarly formatted file would require no changes, and minor differences in the file would require minimal changes.

### Senatorial Elections

Elections for the senate could also be included easily without much change to the code.  We could modify the script to be on a more state rather than county level in order to acheive this.  The amount of data that we would be working with would be significantly larger, but that should work fine with our code.

### Local Elections

We could also use this script to count the ballots of local elections with very little modification.  Many of these elections are separated into different districts at the city, county or state level.  The code would need to be modified accordingly, but it would turn out fine.










