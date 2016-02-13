###################################################################################################################
#
# B R A N D M E I S T E R ' S   R E S T F U L   A P I
#
# Developed by: Jonathan Gonzalez (EA1HET)
# Email: ea1het@ea1het.com
# Date: February 2016
#
# Project URL: http://brandmeister.network
#
###################################################################################################################

from SelfCare import create_app

app = create_app(config_name='development')

if __name__ == '__main__':
    app.run()
