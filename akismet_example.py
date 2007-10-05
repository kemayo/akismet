import akismet

akismet.USERAGENT = "MyApplication/MyVersion"

my_api_key = "SOMETHING"

try:
    real_key = akismet.verify_key(my_api_key,"http://www.example.com")
    if real_key:
        is_spam = akismet.comment_check(my_api_key,"http://www.example.com",
            "127.0.0.1", "Mozilla/5.0 (...) Gecko/20051111 Firefox/1.5",
            comment_content="VIAGRA! LOTS OF VIAGRA!")
        if is_spam:
            print "Yup, that's spam alright."
        else:
            print "Hooray, your users aren't scum!"
except akismet.AkismetError, e:
    print e.response, e.statuscode

# If you're a good person, you can report false positives via akismet.submit_ham(),
# and false negatives via akismet.submit_spam(), using exactly the same parameters
# as akismet.comment_check.