from faker import Faker
import pandas as pd
import random
import math

class GroupGenerator():

    def __init__(self, k_participant, n_course):
        """Initiates the faculty with the attributes: number of participants, number of courses"""
        self.number_participant = k_participant
        self.number_course = n_course
        self.create_participant()
        self.create_course()
        self.random_assignment()
        self.assignment_table()

    def create_participant(self):
        """Returns a list of participants with random fake names"""
        fake = Faker()
        self.list_participant = []
        for _ in range(self.number_participant):
            self.list_participant.append(fake.name())
        return self.list_participant

    def create_course(self):
        """Creates courses with random fake names"""
        fake = Faker()
        self.list_course = []
        for _ in range(self.number_course):
            self.list_course.append(fake.country())
        return self.list_course

    def random_assignment(self):
        """Returns an array with random lists of participants assigned equally to courses"""
        max_group_number = math.floor(self.number_participant / self.number_course)
        self.list_distribute = []
        list_index = [i for i in range(self.number_course)]
        
        # creating participant list for each course
        for course in self.list_course:
            course = []
            for _ in range(max_group_number):
                participant = random.choice(self.list_participant)
                self.list_participant.remove(participant)
                course.append(participant)
            self.list_distribute.append(course)

        # in case participants cant be divided equally into groups
        for _ in range(len(self.list_participant)):
            participant = random.choice(self.list_participant)
            self.list_participant.remove(participant)
            random_index = random.choice(list_index)
            list_index.remove(random_index)
            self.list_distribute[random_index].append(participant) 

        return self.list_distribute

    def assignment_table(self):
        """Returns a dataframe with the courses in columns and participants in rows"""
        df = pd.DataFrame(self.list_distribute).T
        df.columns = self.list_course
        df.index += 1
        return df