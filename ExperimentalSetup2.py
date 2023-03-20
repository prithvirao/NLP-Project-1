from reader.fileReader import read_file
from processor.calcScore import getScores
def evaluate_event2():

    rukwar_gold_standard_path = 'Gold Standard/RussiaUkraineWar.txt'

    rukwar_candidate_file_path = {
    "t5_base_russianwar_60":"Model_summaries/RussiaUkraineWar/T5-base/t5_base_russianwar_60.txt",
    "t5_base_russianwar_80":"Model_summaries/RussiaUkraineWar/T5-base/t5_base_russianwar_80.txt",
    "t5_base_russiawar_100":"Model_summaries/RussiaUkraineWar/T5-base/t5_base_russiawar_100.txt",
    "t5_small_russianwar_60":"Model_summaries/RussiaUkraineWar/T5-small/t5_small_russianwar_60.txt",
    "t5_small_russianwar_80":"Model_summaries/RussiaUkraineWar/T5-small/t5_small_russianwar_80.txt",
    "t5_small_russiawar_100":"Model_summaries/RussiaUkraineWar/T5-small/t5_small_russiawar_100.txt"
    }

    rukwar_gold_standard = read_file(rukwar_gold_standard_path)

    for ref_path in rukwar_candidate_file_path:
        candidate = read_file(rukwar_candidate_file_path[ref_path])
        print(ref_path)
        print('#'*20)
        scores = getScores(rukwar_gold_standard,candidate)
        print(scores) 
