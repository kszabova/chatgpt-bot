# Problems during development

The major problem I encountered is ChatGPT's non-determinism.
For the same prompt, it produced drastically different answers
when I ran it several times. This was a problem, for example,
when I needed to obtain the answer in a given format (one word,
one number, etc.). Designing a prompt that would lead to the
same (or similar) answer turned out to be too difficult and 
the variety of answers was unmanageable for postprocessing,
which is why I set the temperature parameter of the model to 0,
thus making the model produce almost deterministic outputs.

It's relatively hard to get ChatGPT to produce output in the
expected format. While I managed to make it produce just one
word as an answer for yes/no questions, I couldn't create a
prompt that makes it output a single number for selecting an
element from a numbered list. The closest I managed to get
was an answer that contained both the number and the name of
the subtopic. Even for the yes/no questions,
the model would sometimes answer "It's impossible to say..."
and I couldn't find a way to prevent this behavior. Therefore,
when I needed the answer in a specific format, I postprocessed
the model's output and defined default behavior depending on
the specific application.

ChatGPT was very reluctant to engage in chitchat. For questions
such as "What's your favorite food?", it would either answer
"electricity" or "I can't have a favorite food" for most prompts.
I found this part to be the most challenging part of the prompt
design. I finally managed to create a prompt to which the model
gives human-like answers. However, while I tested the prompt
on many questions, there is always another question to which
it fails to give a proper answer. Since there are infinitely
many possible questions, it is impossible to test the prompt
on all of them. Therefore, I settled on a prompt that I 
considered to be good enough.

ChatGPT is very sensitive to even small changes in the prompts.
For example, the answers to "Co je tvoje oblibene jidlo?" and
"Jake je tvoje oblibene jidlo?" were extremely different
for a lot of the prompts I tested. This made prompt design
even more challenging.

Finally, I ran into a problem regarding the Code of Conduct.
The document is in Slovak and I worried that the model would
produce answers in Slovak, but a simple instruction to answer
in Czech actually led to only Czech answers, which was a little
surprising to me. The bigger issue was the fact that the document
is longer than the maximum input length of the model. Therefore,
I split the task of answering questions related to the Code of
Conduct into two parts: first, decide the subtopic of the question
(subtopics are the chapters in the documents), and then answer
the question based on the relevant excerpt. Since the subtopics
were defined only by the name of the chapter, the model sometimes
identified a different one than I would have. This might also
be due to the nature of some of the questions I tested. For instance,
the question "Can I tell my family about the forecast for the next
quarter?" concerns both family and confidential information. It
might not be completely clear which subsection of the document
the model should look into. Fortunately, even when the model
identified a "bad" subtopic, it managed to produce a good answer,
since most of the information in the document is very general.

# Questions

1. Are there any alternatives to ChatGPT in this area and if so, is ChatGPT the
best?

There are other models that are trained for instruction following, such
as text-davinci-003, GPT4, or open-source ones such as Alpaca. Especially
the larger models such as GPT4 are better at following the specified
instruction format (according to this paper: https://arxiv.org/abs/2302.14520).
These models would likely be better at the tasks that involve classifying
the input. However, since ChatGPT is also fine-tuned for chat, it's
probably the best option for general chitchat.

There's also the question of cost and privacy. Since Alpaca produces similar
results to text-davinci-003, it might be a better choice for applications
that require a lot of queries to the model or for applications in industries
where regulations might prohibit third-party software (e.g. medicine).

2. What is the best way to prevent the bot from hallucinating? Is there a way
to let the user know that the answer they have received might not be
correct?

One approach I'm aware of is matching the user's input to a prompt form a set
of manually tested prompts and then using that prompt to query the model.
The likelihood of hallucinations should then be lower since there is much less
variety in the prompts and each prompt can be extensively tested.

Hallucinations of the type "The company has 1000 employees" when, in fact,
it has 10,000 employees could be mitigated by making the model generate
templates and then filling them with data from a database.

One could also employ multi-step generation: instead of generating the answer
directly from the user's input, it could first match the input to a topic,
then retrieve information relevant to the topic from a set of documents, and
use that information as input to the next prompt that generates the final answer.

The creator of the bot can let the user know that the information might be
incorrect by displaying a warning to double-check, perhaps including
a link to a relevant webpage (athough this itself is prone to hallucinations
if generated by a LLM). I'm not aware of any approaches that modify the model
to hallucinate less or that can tell whether an output is factually correct or ot.

3. Could the hallucinations be reduced by feeding it more data?

Yes, fine-tuning the model with company-specific information could
reduce the amount of hallucinations regarding the company.

4. Imagine you actually made such a bot and made it available for chatting. Can
you imagine any drawbacks in the user experience while chatting with this
trained ChatGPT? How would you solve them?

In my experience, the ChatGPT API is quite slow and it takes several seconds
to generate an answer. This is, in my opinion, the biggest problem for
the user experience. The latency might be reduced if we used an on-premise
model (such as the afore-mentioned Alpaca) or if we had a preprocessed
set of answers to common questions, only querying the online API for
previously unseen questions. Another approach is to use smaller models for
easier task (such as Ada) and only use the large, slow models for
difficult tasks.

Another problem might be if a user uses non-standard language (lack of diacritics,
dialects, spelling mistakes). The chatbot might not understand well
(although the understanding would probably not be worse than chatbots that
don't use LLMs), which would lead to frustration. One solution might be 
to pre-process the input using another model (for example one trained for
denoising and fine-tuned on the data that we expect) and use the preprocessed
output to get the answer. However, I'm not sure how big of a problem
such "bad" language is in practice.

Since ChatGPT has a relatively limited maximum input length, we can't keep
long histories of the conversation. Therefore, when the user refers to something
that was said several turns ago, the bot doesn't remember it anymore and
the user must provide the information again. It is possible to solve this
by e.g. using a model that summarizes the entire history of the conversation
into a short text that is then given to ChatGPT; however, for long conversations,
this is impractical and a lot of information would be lost.

The last problem might arise when we try to balance the helpfulness of the
bot and not generating anything untrue or anything that damages the company.
If we set the criteria too strict, the bot will identify many false positives
and will generate meaningless default answers; however, if we set them too
loose, it might generate wrong information or information that paints
the company in a bad light. It requires a large amount of testing to
set the parameters so that they don't interfere with the user experience
too much.

5. How does the bot’s accuracy change by changing the GPT parameters? Are the
default options the best for this use case?

We can change the following parameters for ChatGPT: temperature, maximum length,
top P, frequency penalty, and presence penalty.

Frequency penalty and presence
penalty determine the diversity of the text - i.e. whether the model will try
to talk about new topics or change sentence structure. The default options are
0 for both; this is actually the best option for our use case. For text
classification when we want to get the answer in an expected format, we
don't want any diversity; for questions about code of conduct, it is probably best
that the bot repeats the relevant section verbatim. Some diversity might be
welcome in general chitchat; however, I found that the model is reasonably
creative even without changing these parameters.

Maximum length determines how long an output is. The default value is infinity,
which I changed to 256 which I consider a reasonable length. Each specific
application could have maximum length set to a different value - for example,
we might want the "classifiers" to ouput answers 1 word long. We would
have to find out how many tokens there are in each possible answer and set that
as the maximum length. On the other hand, conversation related to information
about the company might benefit from a longer maximum length.

Temperature determines how deterministic the model is when generating. 0
is close to completely deterministic (although there still is some variance),
which is useful for classifying text when we expect the output in a unified
format. On the other hand, the answers to the user's questions themselves
may be generated more non-deterministically to decrease repetitiveness.

I don't understand the details of the top P parameter, but I understand that
it affects the size of the pool from which the model chooses the next token.
When set to 1, it considers all possible options. Setting it to a lower value
leads to a smaller set of choices which reduces the diversity of the text.
OpenAI documentation recommends not changing the parameter if the temperature
value has been changed and I haven't played much with it, but maybe it
would be useful for the classifying tasks by reducing the number of options,
thus making the output more predictable.

6. Would this bot’s accuracy be improved with GPT-4?

Yes. GPT-4 is better at understanding and following instructions, which means
that it would be less work to get it to output a specified format. It also
takes a much larger maximum input length, which means we could give it long
documents for it to extract relevant information and not split the tasks
into subtopic-classification and generation based on partial information.
We could also make it retain the entire dialogue history, which improves
the user experience in that they don't have to reiterate the details all
the time.
