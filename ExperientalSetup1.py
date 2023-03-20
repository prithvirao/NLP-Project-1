from reader.fileReader import read_file
from processor.calcScore import getScores

def evaluate_event1():
    freddy_gold_standard_path = 'Gold Standard/CycloneFreddy.txt'
    
    freddy_candidate_file_path={
        "t5_base_freddy_60":"Model_summaries/CycloneFreddy/T5-base/t5_base_freddy_60.txt",
        "t5_base_freddy_80":"Model_summaries/CycloneFreddy/T5-base/t5_base_freddy_80.txt",
        "t5_base_freddy_100":"Model_summaries/CycloneFreddy/T5-base/t5_base_freddy_100.txt",
        "t5_small_freddy_60":"Model_summaries/CycloneFreddy/T5-small/t5_small_freddy_60.txt",
        "t5_small_freddy_80":"Model_summaries/CycloneFreddy/T5-small/t5_small_freddy_80.txt",
        "t5_small_freddy_100":"Model_summaries/CycloneFreddy/T5-small/t5_small_freddy_100.txt"
        }

    freddy_gold_standard = read_file(freddy_gold_standard_path)

    for ref_path in freddy_candidate_file_path:
        candidate = read_file(freddy_candidate_file_path[ref_path])
        print(ref_path)
        print('#'*20)
        scores = getScores(freddy_gold_standard,candidate)
        print(scores)
evaluate_event1()