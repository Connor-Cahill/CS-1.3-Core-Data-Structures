
def redact(text: [str], redacted_words: [str]) -> [str]:
    """
    Given 2 arrays of strings returns a new
    array with words from text array that are
    not in redacted words

    COMPLEXITIES:
    ---------------------
    Time Complexity: O(n)
    Space Complexity: O(n)
    ----------------------
    """
    # redacted words lowercased and put into set
    bad_words = set(word.lower() for word in redacted_words)

    # iterate over text and check if each
    # word is in redacted words if not append
    # to our return string
    return [word for word in text if word.lower() not in bad_words]


def test_redact_one():
    text = ['hello', 'there', 'my', 'fuck', 'name']
    bad_words = ['fuck', 'my']
    assert redact(text, bad_words) == ['hello', 'there', 'name']

def test_redact_no_matches():
    text = ['boom', 'hello', 'me']
    bad_words = ['gone', 'wind', 'monday']
    assert redact(text, bad_words) == ['boom', 'hello', 'me']

def test_redact_all_match():
    text = ['hello', 'good', 'goodbye']
    bad_words = ['hello', 'good', 'goodbye']
    assert redact(text, bad_words) == []

if __name__ == '__main__':
    test_redact_one()
    test_redact_no_matches()
    test_redact_all_match()
