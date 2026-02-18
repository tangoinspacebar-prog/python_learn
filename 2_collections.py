# importing library to support generation of random numbers
import random
import string

# 1 create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter
# dict's values should be a number (0-100)

# define list and randomized list length with counter
gen_list = []
gen_list_len = random.randint(2, 10)
print(gen_list_len)

# define loop for list
while len(gen_list) < gen_list_len:
    # prepare dict for processing in a loop
    # list stores pointers to dicts, so i cannot clear same dict for reusage, i need to recreate it (with same name)
    gen_dict = {}
    gen_dict_len = random.randint(2, 10)
    # randomize dict using random dict length, random keys, random values
    # do assignment in the loop, as length is random
    while len(gen_dict) < gen_dict_len:
        gen_dict.update({random.choice(string.ascii_lowercase): random.randint(0,100)})
    # assign result to list
    gen_list.append(gen_dict)
print(gen_list)


# 2. get previously generated list of dicts and create one common dict:
# prepare variables for processing
summary_dict = {}
#tmp_key = '~'
#tmp_value = 0
tmp_skip = False
tmp_modify = False

# take each dict in the list
for i in range(len(gen_list)):
    # for each item in the dict
    for key, value in gen_list[i].items():

        # if already found, skip
        for k, v in summary_dict.items():
            if k.find(key) >= 0:
                tmp_skip = True

        if tmp_skip == True:
            tmp_skip = False
        else:
            tmp_key = key
            tmp_value = value

            # found in cycle max value + define if need to modify key
            for j in range(i, len(gen_list)):
                if key in gen_list[j].keys():
                    if gen_list[j][key] > tmp_value:
                        tmp_value = gen_list[j][key]
                        if j!=i:
                            tmp_key = key+'_'+str(j+1)
                    if j!=i:
                        tmp_modify = True

                if tmp_modify == True:
                    if tmp_key.find('_') == -1:
                        tmp_key = key+'_'+str(i+1)
                    tmp_modify = False

            summary_dict[tmp_key] = tmp_value

        #print(str(i) + ' ' + tmp_key + ' ' + str(tmp_value))
print(summary_dict)

