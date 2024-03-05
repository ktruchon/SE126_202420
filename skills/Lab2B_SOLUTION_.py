#LAB 2B SOLUTION

#PROGRAM PROMPT:
#You are currently working for small start-up company that produces short “How-to” videos.  The company is currently producing videos for customers who need to know how to fix common networking problems. You oversee the company’s network and the owner of the company has just informed you that the company will also be producing “How-to” videos on how to install, configure and manage a Linux OS.  You need to let the owner of the company know if you will have enough storage on your current NAS (Network Attached Storage). You currently have 250 videos stored on your NAS which occupy 1.4 TB of disk space. Your NAS has 8 TB of storage.  The company is currently producing 15 videos a week with an average file size of 5.6 GB.  The company expects to triple that average once they start producing videos for the OS.  If the average file size of each video is 5.6 GB how long will it be before you run out of storage space?  Tell the user how many days left of storage are available just by making their current How-To videos, as well as how many days are left if they started their How-To videos today (which increases the videos being produced weekly 3x) Every output value should be format rounded to the 1st decimal place.

#   [Note: this means you will have TWO possibilities for days left of storage]


#Write a program that will determine how many days of storage is left on the NAS?

#Notes:
#   o	First find the size comparison of Terabytes, Gigabytes, and Bytes
#8 bits = 1 byte
#1000 bytes = 1 kilobyte (KB)
#1000 KB = 1 megabyte (MB)
#1000 MB = 1 gigabyte (GB)
#1000 GB = 1 terabyte (TB)
#1000 TB = 1 petabyte (PB)

#7 days in the week

#VARIABLE DICITONARY------------------------------------------------------------------------------------
#total_store            total storage available on NAS
#used_store             currently used storage on NAS
#avail_store            available storage on NAS, in TB
#avail_storeGB          available storage on NAS, in GB
#videos                 number of videos being uploaded weekly
#vid_size               average video size being uploaded
#weekly_upload          total upload size for the week, in GB
#weeks_left             weeks left in storage based on current weekly_upload
#new_weeks_left         weeks left in storage based on 3x current weekly_upload
#days_left              days left in storage based on current upload, weeks_left * 7
#new_days_left          days left in storage based on 3x current upload




#START PROGRAM-----------------------------------------------------------------------------------------

#storage known values
total_store = 8 #TB
used_store = 1.4 #TB

#video upload known values
videos = 15 #weekly videos
vid_size = 5.6 #GB

#calculate available storage
avail_store = total_store - used_store #TB

#convert available storage into GB
avail_storeGB = avail_store * 1000

#calculate weekly upload 
weekly_upload = vid_size * videos

#calculate weeks left of storage at current upload
weeks_left = avail_storeGB / weekly_upload

#convert weeks to days
days_left = weeks_left * 7

#calculate weeks left of storage at 3x upload 
new_weeks_left = avail_storeGB / (weekly_upload * 3)

#convert weeks to days
new_days_left = new_weeks_left * 7

#print to user final values
print("\n\nStorage currently available on your NAS: {0:.1f}TB/{1:.1f}GB ".format(avail_store, avail_storeGB))
print("\n\t   Days left of storage at current upload: {:.1f}".format(days_left))
print("\n\tDays left of storage at 3x current upload: {:.1f}\n\n\n".format(new_days_left))



