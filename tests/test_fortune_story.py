import pytest
import Fortune_story

class Tests:
    @pytest.fixture
    def sample_name():
        return "Alice"
    def test_True(self):
        "verify that a test that always passes"
        expected = True
        result = True
        assert expected == result, "Should always be true"
    def test_return_length(sample_name):
        "verify that Fortune_story returns 1 story and not multiple"

        result = Fortune_story(sample_name) 
        assert isinstance(result,list), "Should return  a result from our list"
        assert len(result)== 1, "Should contain 1 story from our list"
    

    def test_name_story(sample_name):
        "Verify the sample_name is within the story "
        result= Fortune_story(sample_name)
        assert sample_name in result , "the story should contain the inputted name"
    
    def test_valid_story(sample_name):
        "What is returned should be within our list of stories"
        valid_stories= [
        f"{sample_name} woke up on day to find out that his body was taken over by AI. When he thought of something his body would code it in an instance, but no matter what he did there always bugs",
        f"The universe opens and {sample_name} sees the infinte possiblites of error in his code. After looking through millions of possiblites {name} found the one universe where they fixed their code",
        f"While in the ancient Libary, {sample_name} found the ancient text of auto debugger,they opened the book and it read one line: in order to not have bugs one must not code",
        f"{sample_name} searched far and wide in order to find the Grand AI that would save the world. After finding it the world turned into 1s and 0s and {name} was now the Grand AI"
    ]
        result = Fortune_story(sample_name)
        assert result in valid_stories,"The returned story should be a valid option"
    def test_all_stories(sample_name):
        "Makes sure that all our stories are acceptable"
        stories= [
        f"{sample_name} woke up on day to find out that his body was taken over by AI. When he thought of something his body would code it in an instance, but no matter what he did there always bugs",
        f"The universe opens and {sample_name} sees the infinte possiblites of error in his code. After looking through millions of possiblites {name} found the one universe where they fixed their code",
        f"While in the ancient Libary, {sample_name} found the ancient text of auto debugger,they opened the book and it read one line: in order to not have bugs one must not code",
        f"{sample_name} searched far and wide in order to find the Grand AI that would save the world. After finding it the world turned into 1s and 0s and {name} was now the Grand AI"
    ]
        for i in range(50):
            result = Fortune_story(sample_name)
            assert(result in stories),f"Expected to story to be returned from stories instead it returned{result}"