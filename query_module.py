
def qmod(myquestion):
    def query_wolfram(myquestion):
        #queries wolfram
        import requests
        import wolframalpha
        api_key = "YOUR_WOLFRAM_API_HERE"
        c = wolframalpha.Client(api_key)
        try:
            res = c.query(myquestion)
            solve = next(res.results).text
            return solve
        except Exception as e:
            print("[--]",e)
            return None




    def query(myquestion):
        #queries chatgpt
        import openai
        api_key = "YOUR_OPENAI_API_HERE"
        openai.api_key = api_key
        msg = [{"role": "user", "content": myquestion}]
        try:
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=msg)
            return completion["choices"][0]["message"]["content"]
        except Exception as E:
            print("[-]",E)
            return None







    #queries OpenAI, if it fails it queries Wolfram
    x = query(myquestion)
    if x == None:
        x = query_you(myquestion)


    #talks :) 
    import talker
    if x == None:
        talker.say_it("I'm sorry, I couldn't get the results")
    else:
        talker.say_it(x)












