#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")


raspistill -n -q 100 -o /var/www/html/images/$DATE.jpg
