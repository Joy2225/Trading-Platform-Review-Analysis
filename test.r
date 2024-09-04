library(topicmodels)
library(lda)
library(slam)
library(stm)
library(ggplot2)
library(dplyr)
library(tidytext)
library(furrr) # try to make it faster
plan(multicore)
library(tm) # Framework for text mining
library(tidyverse) # Data preparation and pipes %>%
library(ggplot2) # For plotting word frequencies
library(wordcloud) # Wordclouds!
library(Rtsne)
library(rsvd)
library(geometry)
library(NLP)
library(ldatuning) 


# Clear up data in global environment
rm(list=ls())

# Load data from csv file
sentiments <- read.csv("sentiments.csv")

# Check for NAs
cat("\n")
sapply(sentiments, function(x) sum(is.na(x)))

cat("\n")

# Overview of original dataset
str(sentiments)
cat("\n")
sapply(sentiments, typeof)
cat("\n")


# Set the seed for reproducibility
set.seed(830)

# Sample 1000 rows from the original dataframe
sentiments_sample <- sentiments[sample(nrow(sentiments), 1000), ]

# Convert columns to appropriate formats
sentiments_sample$`Trading app` <- as.factor(sentiments_sample$`Trading app`)
sentiments_sample$Source <- as.factor(sentiments_sample$Source)
sentiments_sample$Comment <- as.character(sentiments_sample$Comment)
sentiments_sample$Sentiment <- as.factor(sentiments_sample$Sentiment)

# Double-check the format of each column
sapply(sentiments_sample, typeof)