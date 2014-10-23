Alive
=====

A simple alive checker cron tool. This is designed to run on Heroku and check every 10 minutes to see if the URLs from the list are still responding. If they fail, it uses the Mandrill email API to send an email.

You will need to setup your own Mandrill account or change the values to another SMTP service.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)