#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -n -o /var/www/html/images/$DATE.jpg
