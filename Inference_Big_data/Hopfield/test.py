from neurodynex.hopfield_network import network, pattern_tools, plot_tools


import numpy as np
import matplotlib.pyplot as plt
import time
network_size=30
start_time = time.time()

alpha_list = np.arange(0.07,0.22,0.020
                      )
m_list = []
hopfield_net = network.HopfieldNetwork(nr_neurons= network_size**2)
factory = pattern_tools.PatternFactory(network_size,network_size)

pattern_list=[]
pattern_list.extend(factory.create_random_pattern_list(nr_patterns=int(alpha_list[-1]*network_size*network_size), on_probability=0.5))

for alpha in alpha_list:
 print (alpha)

# create an instance of the class HopfieldNetwork
 


# let the hopfield network "learn" the patterns. Note: they are not stored
# explicitly but only network weights are updated !
 hopfield_net.store_patterns(pattern_list[0:int(alpha*network_size*network_size)])

# create a noisy version of a pattern and use that to initialize the network
 noisy_init_state=pattern_tools.flip_n(pattern_list[0],nr_of_flips=int(network_size*network_size*0.15)) # 10% of noisy pixels

 hopfield_net.set_state_from_pattern(noisy_init_state)
 states_as_patterns_old =  [noisy_init_state]
 states_as_patterns_new = [pattern_list[0]]
# from this initial state, let the network dynamics evolve.
#hopfield_net.run(nr_steps=50)
 #while pattern_tools.compute_overlap(states_as_patterns_old[0],states_as_patterns_new[0]) < 0.95:
  #print pattern_tools.compute_overlap(states_as_patterns_old[0],states_as_patterns_new[0])
  #states_as_patterns_old = states_as_patterns_new
  #states_new = hopfield_net.run_with_monitoring(nr_steps=1)
  #states_as_patterns_new = factory.reshape_patterns(states_new)
# each network state is a vector. reshape it to the same shape used to create the patterns.
 hopfield_net.run(nr_steps=70)
 states = hopfield_net.run_with_monitoring(nr_steps=1)
 states_as_patterns = factory.reshape_patterns(states)
 m_list.append(pattern_tools.compute_overlap(states_as_patterns[0],pattern_list[0]))
# plot the states of the network
print("--- %s seconds ---" % (time.time() - start_time))

plt.figure()
plt.plot(alpha_list,m_list)
plt.title('Magnetization function of alpha')
plt.savefig('Phase_transition_with_size{}'.format(network_size))
plt.show()


