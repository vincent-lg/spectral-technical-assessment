# Spectral Energy: Technical Assessment

This file, divided in two sections, attempts to describe both the implementation in technical
terms (what I have done) and the process (how I've approached the problem)
in answer to the Technical Test (see the (instructions.md) file for
the list of instructions).

## Implementation

This section describes the technical implementation in terms of end products
(what now exists in this folder).  The section on [#process](Process)
focuses on the steps I took to approach the problem.

## Process

This section focuses on the different steps I took in solving the problem.
Although it wasn't specifically asked, I imagine it is important to have
this information for you and I tried to keep it clear and concise at the same time.

1.  Documentation
    The first step in my work usually focuses on documentation.  I tend to
    rephrase instructions in more technical terms.  I try to identify
    areas where there is a doubt on what I should implement, and decide
    if I can solve these questions myself or if I should ask more
    questions to whoever gave me this mission.  This usually serves
    two purposes: make sure I understood the mission, and clarify as much
    of it in technical terms as possible, when the mission hasn't been
    phrased with technical details in mind.  I consider this step to be
    important, since it will influence a lot of the following steps,
    and my philosophy remains: when in doubt, ask before implementing.
    Regarding the instructions you have provided, I haven't found much
    to question.  The project boundaries were extremely clear and not
    much was open to interpretation.  I found myself wondering
    "shouldn't I add this feature?" and answering to myself that this
    wasn't asked specifically and was probably not the goal.
2.  Bare implementation without microservices
    At this point, the main goal was to arrive at something that works,
    although it did't have to be perfect.  I chose to work in Python for
    simplicity's sake, because I have implemented microservices in this
    language and know the libraries I will need.  It might have been
    a better strategy to develop directly in C#, to show I could do it in
    a different language, but I decided to arrive to the solution with
    what I knew, being confident that I could adapt to C# (or another
    high-level language) without much time.  Of course, this decision
    doesn't imply I cannot work with anything but Python.
    This step involveed creating a "fake" service (though not a microservice)
    and an HTTP server.  I used only standand modules for the former, though I used
    Flask for the latter (and intend to keep using Flask in the next
    step).  The reason why I didn't put them in microservices at this
    point is mostly that it would be easier to test them the way they
    were and make adjustements.
3.  Full implementation with microservices
    Having working code, I separated it in microservices as per instructions.
    I used gRPC to maintain communication between these services.
    One client would be responsible for reading the data from disk and
    sending it.  The other would ask for the data and convert it
    to JSON.  The web server was added in this second client to render
    the JSON response.
4.  Easier deployment with Docker
    At this point, having a few services, I wanted to make sure they could
    be easier to deploy.  I used Docker to create several containers.
    Both would use Python and I took advantage of pipenv to create an
    installation of third-party modules easier to replicate.
4.  Test and adjustment
    At this point I tooik some time to create automated testing.
    Sometimes, I create tests just after writing down documentation,
    in a more Test-Driven-Development approach.  I have worked with a
    Behavior-Driven-Development approach where test were written by
    non-technical teams as well, before I started developing the features.
    In this context I decided to keep tests at the end and adjust as
    was needed.  This is not necessarily the best approach, but I tend
    to believe testing is key, no matter when and as long as it's
    "effective" testing.  It's not unheard of, at this point, to have
    to slightly alter the code to fix bugs, but that's why testing is important.
5.  Wrapping up
    Finally came the final step: checking and consistency measurement.
    I again read the full instructions.  I again read my specifications.
    I made sure my tests were in accordance to what I had written (though
    that was more a check, because I had read these instructions a lot
    at that point during the previous steps).  I fixed documentation
    errors.  Starting from the documentation and other project specifications
    usually means I'm more aware of the project goals, but I need to make
    sure I have aligned with the expressed logic after having worked on
    the implementation.  It was also time for light "integration testing",
    which, at this point, mostly implied deployment with docker-compose
    and manual testing communication between services.  This could
    be elaborated further, though in this case, it should be moved
    to a previous step.

Overall, I believe this is aligned with the way I work on a daily basis,
for personal, open-source or professional projects.  In the end, I adapt
my approach to the mission and the team's expectations, so this describes
mostly what I would have done, being alone.  Of course, with a team of
developers and additional collaboration with other teams, the result
might look pretty different and the process could be altered as well.

I hope that helps, in any case.  Feel free to ask additional questions,
if you have any!

Thank you again,

Vincent J. Le Goff
