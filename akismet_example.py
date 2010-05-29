import akismet

akismet.USERAGENT = "MyApplication/MyVersion"

my_api_key = "SOMETHING"

try:
    ak = akismet.Akismet(my_api_key, "http://www.example.com")
    real_key = ak.verify_key()
    if real_key:
        is_spam = ak.comment_check("127.0.0.1", "Mozilla/5.0 (...) Gecko/20051111 Firefox/1.5",
            comment_content="VIAGRA! LOTS OF VIAGRA!")
        if is_spam:
            print "Yup, that's spam alright."
        else:
            print "Hooray, your users aren't scum!"
    else:
        print "Key is not valid"
except akismet.AkismetError, e:
    print e.response, e.statuscode

# If you're a good person, you can report false positives via akismet.submit_ham(),
# and false negatives via akismet.submit_spam(), using exactly the same parameters
# as akismet.comment_check.
