This is a research project on exploring the probability property of scRNA data and some methods for scRNA denoising.

The research is mostly based on the data offered by *Open Problems in Single-Cell Analysis* (https://openproblems.bio/results/denoising/#description). These scRNA data files are too large to be uploaded on Github thus I didn't put them in the repository. If you're interested in them, you can go to *https://drive.google.com/drive/folders/1M6g2FuknSV_hH2SQstMWNKRrjx1FIiCA?usp=drive_link*. 
Here is the work done before November. Many of the codes lack comments, which is a problem for everyone (including myself). Perhaps at the beginning of next year, when I have some free time, I will review this work and add the missing comments.

# Research Report
This report included my work before Sept. this year. You can roughly know the project via this file.

# exploring probability property
The relevant work is in the folder of *proability property verification*. In conclusion, they're Negative Binomial data.

# Lower dimension and visualization
The relevant work is in the folder of *lower_dim_visual*. In conclusion, the tSNE will perform best and the data should be normalized primarily for better result (log/sqrt norm will help more).

# Denoising and clustering
Most of the content is in *MAGIC*.

# distance/neighbor calculating & acceleration
They're in *MAGIC* & *dis_cal*. sklearn has really strong performance, but I believe BMO-UCB has potential to be faster. 

# articles
There're some representative articles I've found. Much of my works are inspired and based on them.

Due to the lack of data file in this repository, some files might be unable to work normally on your device. I put many jupyter notebooks and my research report (this report including my work before Sept.) so that you can see the results at first. I hope it'll save your time. Because it was a really depressed thing to waste lots of time on others' github project to make it run and finally find it not so useful.
