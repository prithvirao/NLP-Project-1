import rouge
import nltk
from rouge_metric import PyRouge
reference="Russian Air Force Su-27 fighter jets intercept and hit a United States Air Force MQ-9 Reaper drone over the Black Sea, with the collision damaging the drone's propeller and causing the United States to crash the drone into international waters. Poland announces that it will deliver four MiG-29 fighter jets to Ukraine, becoming the first NATO member state to send warplanes to Ukraine. Slovakia announces that it will donate its MiG-29 fighter jets, and supply part of its Kub air-defense system to Ukraine. Russian forces shell Kramatorsk, Donetsk Oblast, with cluster munitions, killing at least two civilians and injuring five others. Russian president Vladimir Putin visits Mariupol, Donetsk Oblast, in Russian-occupied Ukraine, for the first time since the invasion began."
candidate="ukraine says russia faced deadliest day war yet, 1,000 troops killed 24-hour period. today’s loss u.s. air force mq-9 reaper drone black sea reminded treacherous... sanand263: john mearsheimer | russia destroying ukraine. when look cut historical cycle russia attack neighbors... accountability key,” esto... u.s. military reportedly plans to draft 400 troops in ukraine by 2022. @rondesantisfl right ball!!! never gotten involved ukraine's war russia verge nuclear war. ukraine's president says russia is a threat to the u.s. and america. rt @mcfaul: russian air force boasts 1,507 attack aircraft. today, poland became first country make clear send jets ukraine. 4 mig-29 fighter jet s... @bobbafettslave1 @edkrassen russian history is longer than that of the u.s. nato ally is sending four f-16s to kiev 'in coming days' mr khmerkov: @trollstoy88: russia's alleged ukrainian children taken. #svb #russia #ukraine #america #britain # russia kidnapping ukrainian children. deporting adequately descri... rt @ahrferrier. encouraged iran hold us hostages win in... rt @lindyli: republicans colluded egypt steal election jimmy carter russia steal f.."
def getScores(reference, candidate):
    evaluator = rouge.Rouge(metrics=None,
                            stats=None, return_lengths=False,                  
                            raw_results=False, exclusive=True)

    ROUGEscores = evaluator.get_scores(candidate, reference)

    return ROUGEscores
