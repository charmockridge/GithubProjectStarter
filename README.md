# Installation

This program is for Mac and Linux Distributions!

Open terminal, and in a directory of your choice, paste:<br>git clone https://github.com/charmockridge/MacGithubProjectStarter.git<br>Then, if you don't have PyGithub or you are unsure, in the terminal paste:<br>pip install PyGithub<br>


# Set Up

In the text editor of your choice, open both start.py and the script file. In the script file, on lines 5, 7 and 12. Edit the line 5 so it matches your path to your projects folder leaving /Users/ and /$1 as it is and the URL on line 7 matching your Github profile's link leaving /$1.git on the end. You may have to delete line 12 if you don't have a terminal command that opens your preferred editor, if you do then just simply change the line to that command. In the start.py file, edit lines 6, 7 and 8 so line 6 matches the path to your projects folder, line 7 so it matches the username of your Github account and line 8 so it matches the password of your Github account.

Next in your finder/file explorer you will have to navigate to the directory where it stores the script file. Once located, right click or CTRL+click on the script file, then select the "Get Info" option. Scroll to the bottom of the page that has just popped up, there should be a padlock. You are going to click on that padlock and you will be prompted to enter the administrative password. Once enterd, open the terminal and navigate to the folder with the script file. Then enter the following into the terminal:<br>chmod 700 script<br>Finally, in your terminal you will need to go to the home directory by typing:<br>cd<br>Then you will want to type:<br>vim .bash_profile<br>You will be then put into a terminal text editor. Using the arrow keys navigate to a free line and press i. This will put you into insert mode allowing you to write. Then paste the following onto the line:<br>alias start='cd; ./script'<br>Once written, press the escape button on the keyboard and type the following:<br>:wq<br>You are now ready to use the script!


# Usage

In order to use the script you need to sudo bash the terminal. You then can write, in the terminal:<br>start projectNameHere<br>Where projectNameHere is the actual name of your project (do not use spaces). A new repository will be made on your Github and a folder in your projects folder will be made in the name of your project with a README.md file in it (this folder will be linked to your repository already) as well as your preferred editor opening up if you have changed line 12 in the script file.

Enjoy!
