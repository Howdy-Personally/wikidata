import bz2
import time
import argparse

def load_10000_line(wikidata_path,line_100_file):
 #load
    with bz2.open(wikidata_path, 'r') as pf:
        j = 0
        for line in pf:
            j+=1
            try:
                unwashed_line = str(line)
                unwashed_line = unwashed_line[2:-4]
                #time.sleep(1)
                if len(unwashed_line)==0:
                    continue
                
                line = unwashed_line

                if j%10002==0:
                    break

                with open(line_100_file,'a')as f:
                    f.write(line+'\n')

            #load
            except Exception :
                print(j,'error')
                pass

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--wikidata_path', type=str, default='D:/latest-all.json.bz2', help='wikidata path')
    parser.add_argument('--store_path', type=str, default='C:/Users/123/Desktop/wikidata/line_10000_file.json', help='store path')
    
    opt=parser.parse_args()
    
    print(time.asctime())
    load_10000_line(opt.wikidata_path,opt.store_path)
    print(time.asctime())