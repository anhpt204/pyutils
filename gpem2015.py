'''
Created on Oct 29, 2014

@author: tuananh
'''
import os, csv, sys

import matplotlib.pyplot as plt
import numpy as np
from os.path import join

problems = [
            #"keijzer-1",
            "keijzer-4",
            "keijzer-6",
            #"keijzer-7",
            #"keijzer-8",
            #"keijzer-9",
            #"keijzer-10",
            "keijzer-11",
            "keijzer-12",
            #"keijzer-13",
            "keijzer-14",
            "keijzer-15",
            
            #"casp",
            #"slump_test_FLOW",
            #"slump_test_Compressive",
            "slump_test_SLUMP",
               
            #"airfoil_self_noise",
            "ccpp", 
            #"concrete", 
            "winequality-red",
            "winequality-white", 
            #"wpbc"
            ]

class_problems = [
                  "EEGEyeState",
                  "breast-cancer-wisconsin", #AGX
                  "data_banknote_authentication",
                  "haberman",
                  "magic04",
                  "wdbc"
                  ]

algs = [
        "SC", 
        "SSC", "MSSC",
        "SGXMSSC", "SGXMMSSC",
        "SGXM", 
        "SGXMSC", 
#         "AGX", "RDO"
        ]

configs = {
            "SC":[],
            "SSC":[],
            "MSSC":[],           
            "SGXM": ["TR-2"],
            "SGXMSC":['bo80'],
            "SGXMSSC":[],
            "SGXMMSSC":[],
            "AGX":["1000"],
            "RDO":["1000"]          
#            "SGXMSC":["tune-0.3-10", "tune-0.3-15", "tune-0.3-20", "tune-0.3-25", "tune-0.3-30",
#                      "tune-0.1-20", "tune-0.2-20", "tune-0.4-20", "tune-0.5-20"], 
           }

root_dir = "/home/tuananh/Documents/projects/GParray/src/"

output_dir = "/home/tuananh/Documents/projects/GParray/out/"

def getAll(file_name, row_number):
    '''
    Get data from files *.all
    '''
    
    output_file = os.path.join(output_dir, file_name)
    print output_file
    
    out = csv.writer(open(output_file, 'w'), quoting=csv.QUOTE_ALL)
    
    row_header1 = [" "]
    row_header2 = [" "]
    #row_header3 = [" "]
    for alg in algs:
        row_header1.append(alg)
        #each alg has two config
        row_header1.append(" ")
        for config in configs[alg]:
            row_header2.append(config)
     #       row_header3 += ["ACC", "TP", "TN", "FP", "FN"]
            
    out.writerow(row_header1)
    out.writerow(row_header2)
    #out.writerow(row_header3)
     
    row = []
    for p in problems:        
        file_name = p + ".all"
        
        print file_name
        
        row.append(p)        
        for alg in algs:
            for config in configs[alg]:
                file_path = os.path.join(root_dir, alg, "out", config, file_name)
                lines = open(file_path).readlines()
                row.append(lines[row_number])
        out.writerow(row)
        row = []
    
                
def getAllClassification(file_name, row_number):
    '''
    Get classification result from files *.all
    '''
    
    output_file = os.path.join(output_dir, file_name)
    out = csv.writer(open(output_file, 'w'), quoting=csv.QUOTE_ALL)
    
    row_header1 = [" "]
    row_header2 = [" "]
    row_header3 = [" "]
    for alg in algs:
        row_header1 += [alg] +[" ", " ", " ", " "]*len(configs[alg]) + [" "]
        for config in configs[alg]:
            row_header2 += [config, " ", " ", " ", " "]
            row_header3 += ["ACC", "TP", "TN", "FP", "FN"]
            
    out.writerow(row_header1)
    out.writerow(row_header2)
    out.writerow(row_header3)
     
    row = []
    for p in class_problems:        
        file_name = p + ".all"
        
        #print file_name, 
        
        row.append(p)        
        for alg in algs:
            #print alg, 
            
            for config in configs[alg]:
                file_path = os.path.join(root_dir, alg, "out", config, file_name)
                lines = open(file_path).readlines()
                vs = lines[row_number].split()
                
                ts = float(vs[1]) + float(vs[2])
                ms = float(vs[1]) + float(vs[2]) + float(vs[3]) + float(vs[4])
                vs[0] = ts/ms
                
                row += vs
                
        out.writerow(row)
        row = []
        
def getTime():
    '''
    Get data from files *.all
    '''
    algs = {
            "AGX":["lib500", "lib1000"],
            "RDO":["lib500", "lib1000"],
            "SGXMSC":["pop500", "pop1000"]
            }
    
    file_name = "time.csv"
    output_file = os.path.join(output_dir, file_name)
    out = csv.writer(open(output_file, 'w'), quoting=csv.QUOTE_ALL)
    
    row_header1 = [" "]
    row_header2 = [" "]
    #row_header3 = [" "]
    for alg in algs:
        row_header1 += [alg] + [" "]*(len(configs[alg]) * 3 - 1)
        for config in configs[alg]:
            row_header2 += [config, " ", " "]
            
    out.writerow(row_header1)
    out.writerow(row_header2)
    #out.writerow(row_header3)
     
    row = []
    for p in problems:        
        file_name = p + ".time"
        
        print file_name
        
        row.append(p)        
        for alg in algs:
            for config in configs[alg]:
                file_path = os.path.join(root_dir, alg, "out", config, file_name)
                lines = open(file_path).readlines()
                vs = lines[0].split()
                row += vs
        out.writerow(row)
        row = []

def get5(problem):
    '''
    Get data from files *.5
    '''
    file_name = problem + ".5"
    
    output_file = os.path.join(output_dir, file_name + ".csv")
    out = csv.writer(open(output_file, 'w'), quoting=csv.QUOTE_ALL)
    
    row_header1 = []
    row_header2 = []
    #row_header3 = [" "]
    for alg in algs:
        row_header1.append(alg)
        #each alg has two config
        row_header1 += [" "]* (len(configs[alg]) * 2 -1)
        for config in configs[alg]:
            row_header2.append(config)
            row_header2.append(" ")
     #       row_header3 += ["ACC", "TP", "TN", "FP", "FN"]
            
    out.writerow(row_header1)
    out.writerow(row_header2)
    out.writerow([])
    out.writerow([])
    #out.writerow(row_header3)
     
    rows = []
    for i in xrange(100):
        rows.append([])
    
         
    for alg in algs:
        for config in configs[alg]:
            file_path = os.path.join(root_dir, alg, "out", config, file_name)
            lines = open(file_path).readlines()
        
            for i in xrange(len(lines)):        
                rows[i] += lines[i].split()
    for row in rows:
        out.writerow(row)
            
def makeConfigFile():
    config_problems = {
            "keijzer-1":[1, 100, 100],
            "keijzer-4": [1, 100, 100],
            "keijzer-6": [1, 100, 100],
            #"keijzer-7": [1, 100, 100],
            "keijzer-8": [1, 100, 100],
            "keijzer-9": [1, 100, 100],
            "keijzer-10": [2, 100, 100],
            "keijzer-11": [2, 100, 100],
            "keijzer-12": [2, 100, 100],
            "keijzer-13": [2, 100, 100],
            "keijzer-14": [2, 100, 100],
            "keijzer-15": [2, 100, 100],
            
            "casp": [9, 100, 100],
            "slump_test_FLOW": [7, 50, 53],
            "slump_test_Compressive": [7, 50, 53],
            "slump_test_SLUMP": [7, 50, 53],
               
            "airfoil_self_noise": [5, 100, 100],
            "ccpp": [4, 200, 200], 
            "concrete": [8, 200, 200], 
            "winequality-red": [11, 250, 250],
            "winequality-white": [11, 300, 300], 
            "wpbc": [31, 100, 98]
            
            }
    
    for k,v in config_problems.items():
        file_name = k + ".param"
        f = open(file_name, 'wb')
        
        lines = []
        lines.append("NUMFITCASE="+ str(v[1]))
        lines.append("NUMFITTEST=" + str(v[2]))
        lines.append("NUMVAR=" + str(v[0]))
        lines.append("NRUN=50")
        lines.append("POPSIZE=500")
        lines.append("NUMGEN=100")
        lines.append("TREELIB_SIZE=500")
        
        lines = [line+"\n" for line in lines]
        
        f.writelines(lines)
        
        
def vehinh(problem, index):
    file_name = problem + ".gen"
    ys = []
    
    algs = ["SC", 
            #'SGXM', 
            "SGXMSC", "AGX", "RDO"]
    
    for alg in algs:
        y = [alg]
        config = configs[alg][0]
        file_path = os.path.join(root_dir, alg, "out", config, file_name)
        lines = open(file_path).readlines()
        for line in lines:
            if(len(line) > 5):
                vs = line.split()
                y.append(float(vs[index]))
        print len(y)
        ys.append(y)
    
    x = [i for i in xrange(100)]
    
    print len(x)
    for y in ys:
        plt.plot(x, y[1:], label=y[0])
            
    
    plt.legend(loc='upper left')
    #dashes = [10, 5, 100, 5] # 10 points on, 5 off, 100 on, 5 off
    #line.set_dashes(dashes)
    plt.grid(True)
    
    plt.xlabel('Generations')
    plt.ylabel('Size')
    plt.title(problem)

    plt.show()
    
from scipy.stats import friedmanchisquare, wilcoxon
import numpy as np

def stat_test_average():
    dir = '/home/pta/Documents/gpem2015/'
    out_file = 'statTestAve1.train'    
    out = open(out_file, 'wb')
        
    measures = []
    measures_dict = {}
    
    for alg in algs:
        key = alg
        measurement = []
        cof = ''
        if configs[alg]:
            cof = configs[alg][0]
            key = alg + '-' + cof
        for problem in problems:
            file_name = problem + '.all.txt'
            file_path = join(dir, alg, cof, file_name)
#             print file_path
            # read data
            lines = open(file_path).readlines()
            # 0 for training, 2 for testing
            measurement.append(float(lines[0]))
            
        measures.append(np.array(measurement))
        print key, measurement
        measures_dict[key] = measurement
        
    ms = np.array(measures)
    r = friedmanchisquare(*measures)
    print 'friedman test: ', r
    out.write('friedman test p-value: {}\n'.format(r[1]))
    # wilcoxon test
        
    out.write('Wilcoxon test \n')

    items = measures_dict.items()
    n_items = len(items)
    for i in xrange(n_items-1):
        k1,v1 = items[i]
        for j in xrange(i+1, n_items):
            k2, v2 = items[j]        
            test = wilcoxon(v1, v2, zero_method='zsplit', correction=True)
            out.write('{}->{}: {} \n'.format(k1, k2, test[1]))
    
    out.close()

def stat_test_run():
    dir = '/home/pta/Documents/gpem2015/'
    out_file = 'statTestRun1.test'    
    out = open(out_file, 'wb')
        
    measures = []
    measures_dict = {}
    
    for alg in algs:
        key = alg
        measurement = []
        cof = ''
        if configs[alg]:
            cof = configs[alg][0]
            key = alg + '-' + cof
        for problem in problems:
            file_name = problem + '.run.txt'
            file_path = join(dir, alg, cof, file_name)
            print file_path
            # read data
            lines = open(file_path).readlines()
            
            n = 20
            if problem == 'keijzer-11':
                n = 10
#             block=[]
            for i in xrange(0,n,2):
                vs = lines[i].split()
                # 0 for training, 1 for testing
                measurement.append(float(vs[1]))
            
#             measurement.append(block)
            
        measures.append(np.array(measurement))
        
        measures_dict[key] = measurement
        
    ms = np.array(measures)
    r = friedmanchisquare(*measures)
    print 'friedman test: ', r
    out.write('friedman test p-value: {}\n'.format(r[1]))
    # wilcoxon test
        
    out.write('Wilcoxon test \n')

    items = measures_dict.items()
    n_items = len(items)
    for i in xrange(n_items):
        k1,v1 = items[i]
        for j in xrange(i+1, n_items):
            k2, v2 = items[j]        
            test = wilcoxon(v1, v2)
            out.write('{}->{}: {} \n'.format(k1, k2, test[1]))
    
    out.close()
    
    
def wilcoxonTest():
    dir1 = '/home/pta/Documents/gpem2015/SGXMSC/durangbuoc/'
    dir2 = '/home/pta/Documents/gpem2015/SGXM/TR-4/'
    
    alg1='SGXMSC' 
    alg2='SGXM-TR4'
    
    out_file = '/home/pta/Documents/gpem2015/' + alg1 + '_' + alg2 + '.test'
    
    out = open(out_file, 'wb')
    
    for problem in problems:
        lines1 = open(os.path.join(dir1, problem + ".run.txt")).readlines()
        lines2 = open(os.path.join(dir2, problem + ".run.txt")).readlines()
        
        x_train = []
        y_train = []
        x_test = []
        y_test = []
        for line1, line2 in zip(lines1, lines2):
            if(len(line1) <2 and len(line2) < 2):
                continue
            xs = line1.split()
            x_train.append(float(xs[0]))
            x_test.append(float(xs[1]))
            
            ys = line2.split()
            y_train.append(float(ys[0]))
            y_test.append(float(ys[1]))
            
        
        train = wilcoxon(x_train, y_train)
        test = wilcoxon(x_test, y_test)
        out.write('{}: {} {} \n'.format(problem, train[1], test[1]))
    
def rdo_paper_stat_test():
    agx3=[0.0117, 0.0235, 0.0110, 0.0091, 0.0108, 0.0000, 0.0016, 0.0059, 0.0371]
    agx4=[0.0018, 0.0023, 0.0011, 0.0007, 0.0002, 0.0003, 0.0002, 0.0004, 0.0127]
    agxp=[0.0005, 0.0031, 0.0023, 0.0012, 0.0016, 0.0002, 0.0002, 0.0007, 0.662]
    # testing
    SC= [19.033611091079603, 5.191174153117511, 18.311988945443204, 11.026278490273599, 24.509214220903406, 7.847092373677867, 442.8457174534556, 3422.3304949842045, 220.5394947788671, 231.1832396122744]
    SSC= [14.846797740021998, 2.444591642479246, 14.206866444244535, 10.79819552015685, 13.573390349623165, 4.966271524408962, 398.0472306622525, 1289.9247951864927, 218.08039187410853, 215.73139950461058]
    MSSC= [12.9390352260084494, 2.762542877154367, 13.2855060089577455, 9.813130376264459, 11.262872048887373, 5.507144948339964, 389.1005005504661, 1134.1162234948374, 219.6148246720252, 218.23381689672334]
    SGXMSSC= [4.301433695388513, 1.3143799125794473, 5.522683432291597, 7.404324947979264, 8.930370142185488, 3.7856781384748084, 535.6187510498205, 1306.1013243443524, 195.7255732002846, 203.50838252377503]
    SGXMMSSC= [2.0738460857220256, 1.7390712494291856, 4.6955492050275645, 3.5448848182543977, 4.7502911546056845, 2.386683672948668, 512.8000805170955, 1011.873070195555, 190.40475642203205, 206.3035050506968]
    SGXM_TR_2= [20.443957451524373, 58.23935700792145, 33.75270542943797, 42.12756563325986, 80.88989205125284, 50.199934141309825, 526.4870050300317, 49150.36999999997, 728.3453557257226, 1213.239168627514]
    SGXMSC_bo80= [3.872036344531763, 1.6368682241516683, 7.55965665214591, 5.792905847527903, 5.6375300734650855, 3.135049538374349, 494.6313263296081, 1152.8961357250246, 204.7356414827818, 202.96215105494255]

    # training
#     SC =[4.861648691408663, 2.210569828682872, 7.133075827207946, 10.34295404203834, 6.88140117724345, 2.9917903275807327, 200.39641151445448, 2085.4973835459755, 105.41733779415391, 174.2213686991353]
#     SSC =[4.742560295415911, 2.170799368982985, 7.761508401772592, 10.115885063123416, 5.658375166481407, 2.529692685711052, 195.7847075928762, 2015.08964195031, 106.60884471431889, 175.52404091084725]
#     MSSC =[4.393888507334641, 1.8229248863197093, 6.689782194497913, 9.069517137648978, 5.1173620043688395, 2.6504008613679797, 189.0450209609006, 1851.9456432946283, 105.24580091720578, 172.98191392808673]
#     SGXMSSC =[4.006478304905582, 1.6692438317324914, 3.8411057518351868, 4.93955531660913, 2.2188376910748007, 2.1063924224848902, 143.50864117920264, 806.5455846605371, 104.61471010038947, 169.2267711316684]
#     SGXMMSSC =[1.9166670293113088, 1.6706044484955658, 2.620048033518452, 2.6597366539355303, 1.7180682646135221, 1.114407836053598, 151.96369024768154, 772.1316060877863, 102.11624941742704, 166.66356045448825]
#     SGXM_TR_2 =[8.718279089518644, 2.795001149262583, 6.398911578880449, 11.816545277477951, 13.667340798566864, 6.107106820757651, 284.88462510516104, 2004.6067756517218, 103.57659240070771, 171.51940893229735]
#     SGXMSC_bo80 =[4.011414043432087, 1.6986726013195508, 5.470143362857626, 4.685569961632392, 3.0851713294123853, 1.9905123321956297, 163.23192204952844, 931.4397891911782, 107.03490716472194, 173.16422909526634]

#     print wilcoxon(agx3, agxp)

    measures = [np.array(x) for x in [SC, SSC, MSSC, SGXMSSC, SGXMMSSC, SGXMSC_bo80]]
    measures_dict = {'sc':SC,
                     'ssc':SSC,
                     'mssc':MSSC,
                     'sgxmssc':SGXMSSC,
                     'sgxmmssc':SGXMMSSC,
                     'sgxmsc_bo80':SGXMSC_bo80}
    
    out = open('statsTestAve.test', 'w')
    
    ms = np.array(measures)
    r = friedmanchisquare(*measures)
    print 'friedman test: ', r
    out.write('friedman test p-value: {}\n'.format(r[1]))
    # wilcoxon test
        
    out.write('Wilcoxon test \n')

    items = measures_dict.items()
    n_items = len(items)
    for i in xrange(n_items):
        k1,v1 = items[i]
        for j in xrange(i+1, n_items):
            k2, v2 = items[j]        
            test = wilcoxon(v1, v2)
            out.write('{}->{}: {} \n'.format(k1, k2, test[1]))
            
            
    out.close()
              
if __name__ == '__main__':
    #makeConfigFile();

    #getAll("fitness.csv", 0)
    #getAll("fittest.csv", 2)
    #getAll("size.csv", 4)
    #getAll("time.csv", 6)
    
    #TIME
    #getTime()
    
    #CLASSIFICATION
#    root_dir = "/home/tuananh/Documents/projects/GPClassification/src/"
#    getAllClassification("cfitness.csv", 0)
#    getAllClassification("cfittest.csv", 2)
    #getAll("csize.csv", 4)
    #getAll("ctime.csv", 6)
    
    #CHILDREN - PARENT
    #root_dir = "/home/tuananh/Documents/projects/GPChildrenParent/src/"
    #for problem in problems:
    #    get5(problem)
    
    
    #vehinh("slump_test_SLUMP", 0)
#     vehinh("keijzer-4", 2)

#     stat_test_average()
    
#     stat_test_run()
    rdo_paper_stat_test()
    
    
    print "DONE"