Windows Helper
==============

MailTo.bat needs to be modified so that baseuri reflects what you need.

MailTo.reg needs to be imported.  I recommend deleting the mailto tree and importing it.

You will need to modify the registry entry to point to the correct location for MailTo.bat.

Test with

```start "mailer" "mailto:myself@mycompany.com"``` at the command line
