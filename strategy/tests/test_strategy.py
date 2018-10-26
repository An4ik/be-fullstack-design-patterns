from unittest import TestCase

from strategy import JobStrategyAbstract, DeveloperStrategy, TeacherStrategy, DoctorStrategy, Man, Woman

class StrategyTest(TestCase):
    def test_instance(self):
        """
        Make sure that Person instance's job attribute is instance of JobStrategyAbstract.
        """
        person = Man("Alex", DeveloperStrategy())
        self.assertTrue(isinstance(person.job, JobStrategyAbstract))

    def test_subclass_DeveloperStrategy(self):
        """
        Make sure that DeveloperStrategy is subclass of JobStrategyAbstract.
        """
        self.assertTrue(issubclass(DeveloperStrategy, JobStrategyAbstract))

    def test_subclass_TeacherStrategy(self):
        """
        Make sure that TeacherStrategy is subclass of JobStrategyAbstract.
        """
        self.assertTrue(issubclass(TeacherStrategy, JobStrategyAbstract))

    def test_subclass_DoctorStrategy(self):
        """
        Make sure that DoctorStrategy is subclass of JobStrategyAbstract.
        """
        self.assertTrue(issubclass(DoctorStrategy, JobStrategyAbstract))

    def test_init(self):
        """
        Make sure that Man or Woman's instances initialize and __str__ magic function outputs correct result. 
        """
        person = Woman("Ann", DeveloperStrategy())
        self.assertEqual(str(person), "Ann is a woman and is working as a Developer at Google.")

    def test_attribute_can_be_changed_at_runtime(self):
        """
        Make sure that Man or Woman's instance's job attribute and it's implementation can be changed at runtime.
        """
        person = Man("Alex", DeveloperStrategy())
        person.job = DoctorStrategy()
        self.assertEqual(str(person), "Alex is a man and is working as a Doctor in hospital.")
