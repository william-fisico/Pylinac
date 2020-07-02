###########################################
# William A. P. dos Santos                #
# william.wapsantos@gmail.com             #
# Testanto Pylinac                        #
# 02 de julho de 2020                     #
###########################################

from pylinac import PicketFence


#PicketFence.run_demo()
pf = PicketFence.from_demo_image()
pf.analyze(tolerance=0.05, action_tolerance=0.03)
# print results to the console
print(pf.results())
# view analyzed image
pf.plot_analyzed_image()
# saver PDF report
#pf.publish_pdf(filename='Demo Picket Fence.pdf')