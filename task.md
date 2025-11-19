This page presents the deliverable for weeks 47 and 48 (Tue 18.11.–Fri 28.11.).

You shall prepare this deliverable together with your collaboration partner.
Working with Git to document your work in small increments and to document collaboration is essential.
Create a NEW Gitlab repository for this exercise!
By the deadline on Friday, 28. November, 18.00, you shall 
create a new repository on Gitlab
call it d4_name1_name2, where name1 and name2 are your first names
give heplesser access to the respository
you can in principle work on Github, but you have to figure out issues, milestones, pull requests and actions there on your own
create issues and milestones in Gitlab to plan the work on your project, connecting issues to milestones
develop code and tests as described below
build a python package (wheel)
run in a terminal 
git log > d4.log
record a short video (at most 3 minutes) in which you explain how the last version of your code works. The video shall show your code. Both partners in a team shall comment on the code. I encourage you to also turn on the camera while recording, so we can see you in the video.
upload the following files to Canvas
A README.md file with a link to your repository
the walk-x.y.z-py3-none-any.whl wheel file containing your code
the log file d4.log
your video
You are encouraged to use the material in https://gitlab.com/heplesser/chutesLinks to an external site. as a starting point and are allowed to copy any files from there, provided you declare the source of the material. In particular, use the pyproject.toml and gitlab-ci.yml files as a starting point.
You hand in as a group delivery, i.e., only one of you needs to upload
All README and code files need to contain your names. In the video, please state your names. Otherwise, credit will be deducted.
Late delivery
3 points will be deducted for up to six hours (i.e. 23:59 on Friday night)
no credit will be given for deliveries that are handed in after that.
Missing video
3 points will be deducted for a missing video.
If you do not have a collaboration partner and need to work alone, please see Instructions for working alone on deliverables.
Walking home from AudMax (Samfunnet)
Consider the following situation: After a long night of partying, student Alex wants to go home. We assume here that Ås is a one-dimensional world, stretching from E6 in the west (coordinate 0) to the railway line in the east (coordinate 100). Along this axis, we have, from west to east, Pentagon dorms, AudMax, and Kaia dorms. Due to the aftereffects of heavy partying, Alex' walk home is not too steady. Specifically, Alex proceeds as follows:

Ås has only discrete, integer coordinates from 0 (E6) to 100 (railway). Place Pentagon, AudMax and Kaia suitably in between.
Time is counted in whole seconds.
Every second, Alex takes a step with 20% probability.
If Alex takes a step, it is with 50% probability to the east and with 50% to the west. The number of steps taken is counted.
When Alex is at the location of Pentagon, Alex will enter and stay at Pentagon with probability p_pentagon. Then, Alex has arrived and the simulation is over. Correspondingly, when Alex is at Kaia, Alex will stay at Kaia with probability p_kaia.
We are interested in
whether Alex ends up at Kaia or Pentagon
how many seconds and how many steps it takes Alex to get to either Kaia or Pentagon
and how these results depend on p_pentagon and p_kaia.
 

Task 1 (4 points): The simulation
Implement the simulation with a similar code structure as the chutes package: An importable package with different classes in different files, and an example file running a simulation and presenting results. The example should run a large number of simulations and provided statistics on the results.
Develop this code in multiple steps, using Gitlab issues and milestones to structure your work. Individual steps should be developed in branches and merged on Gitlab using merge requests. Partners shall review their code mutually.
 

Task 2 (4 points): Testing and shipping
Create a testsuite for your code. Aim for at least 80% coverage.
Configure your project for packaging using a pyproject.toml file. The file shall include a tox section to run both flake8 format checks and the testsuite you have created.
Create a .gitlab-ci.yml file to run the tests automatically when you push to GitLab (if GitLab requests a credit card or similar, give this file a similar but different name to show you did the work; no need to give your credit card to GitLab!).
Ensure that python -m build creates a complete package including all your material.
 

Task 3 (2 points): Explore the model
Create a Jupyter notebook in which you run simulation for different values of p_kaia and p_pentagon. Show the results, preferably also graphically and describe your observations. The notebook should go to the examples directory.
Make sure that the notebook is included in the package your build.