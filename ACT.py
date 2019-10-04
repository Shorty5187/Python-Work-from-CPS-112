class ACT:

    def __init__(self, english, math, reading, science):
        if english < 1 or english > 36:
            raise Exception('English must be 1..36')#repeat this for each test score

        self.english = english
        self.math = math
        self.reading = reading
        self.science = science

    def __str__(self):
        return "English: {}, Math: {}, Reading: {}, Science: {}".format(self.english, self.math, self.reading, self.science, self.composite)


    @property
    def composite(self):
        return round( (self.english + self.math + self.reading + self.science + 0.01) / 4 )

class ACTScores:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add(self, score):
        self.scores.append(score)

    def __str__(self):
        return self.name + "\n" + "\n".join( [str(act) for act in self.scores] )

    @property
    def max_english(self):
        return max(act.english for act in self.scores)

        # cur_max = self.scores[0].english
        # for i in range(1, len(self.scores)):
        #     if self.scores[i].english > cur_max:
        #         cur_max = self.scores[i].english
        #     return cur_max

    @property
    def max_math(self):
        return max(act.math for act in self.scores)

    @property
    def max_reading(self):
        return max(act.reading for act in self.scores)

    @property
    def max_science(self):
        return max(act.science for act in self.scores)

    def composite_act(self):
        return ACT(self.max_english, self.max_math, self.max_reading, self.max_science)


# data= [13,4,2,69,58,4035]
# m = max(data)
# print(m)
#
# exit()
# str1 = "John, Joe, Sue, Sally"
# people = str1.split (',')
# print(people)


# act = ACT(23, 20, 24, 19)

# print( act )
# print(act.english)
# print( act.composite )

act_scores = ACTScores("JDenny: ")
act_scores.add(ACT(23,20,24,19))
act_scores.add(ACT(20,21,24,19))
act_scores.add(ACT(19,18,24,19))
act_scores.add(ACT(24,20,24,22))
print( act_scores )

print ( "Max English", act_scores.max_english)
print ( "Max Math", act_scores.max_math)
print ( "Max Reading", act_scores.max_reading)
print ( "Max Science", act_scores.max_science)
