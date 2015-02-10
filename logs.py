Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> if True:
	print("hello")
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
a
2
hello
>>> range(5)
range(0, 5)
>>> ================================ RESTART ================================
>>> 
a
2
hello
0
1
2
3
4
5
6
7
8
9
>>> ================================ RESTART ================================
>>> 
a
2
hello
0
1
2
3
4
5
6
7
8
9
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
Traceback (most recent call last):
  File "/home/student/Danya/classwork/loops.py", line 9, in <module>
    print(x)
  File "/usr/lib/python3.4/idlelib/PyShell.py", line 1342, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
>>> fib1(1)
1
>>> fib1(2)
1
>>> fib1(6)
8
>>> ================================ RESTART ================================
>>> 
>>> fib1(6)
8
>>> help(fib1)
Help on function fib1 in module __main__:

fib1(n)
    Return n-th Fibonacci number.
    
    Example:
    >>> fib1(1)
    1
    >>> fib1(2)
    1
    >>> fib1(6)
    8

>>> import doctest
>>> import loop
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    import loop
ImportError: No module named 'loop'
>>> import loops
>>> doctest.testmod(loops)
TestResults(failed=0, attempted=3)
>>> help(loops)
Help on module loops:

NAME
    loops

DESCRIPTION
    ##for x in ["a", 2, "hello"]:
    ##    print(x)
    ##
    ##for x in range(10):
    ##    print(x)
    ##
    ##import itertools
    ##for x in itertools.count(1):
    ##    print(x)

FUNCTIONS
    fib1(n)
        Return n-th Fibonacci number.
        
        Example:
        >>> fib1(1)
        1
        >>> fib1(2)
        1
        >>> fib1(6)
        8

FILE
    /home/student/Danya/classwork/loops.py


>>> ================================ RESTART ================================
>>> 
__main__
>>> import loops
loops
>>> import loops
>>> import os
>>> os.path
<module 'posixpath' from '/usr/lib/python3.4/posixpath.py'>
>>> import sys
>>> sys.path
['/home/student/Danya/classwork', '/home/student', '/usr/bin', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']
>>> import x
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    import x
ImportError: No module named 'x'
>>> sys.path.append('..')
>>> import x
>>> ================================ RESTART ================================
>>> 
__main__
>>> import doctest
>>> import loops
loops
>>> dotest.testmod(loops)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    dotest.testmod(loops)
NameError: name 'dotest' is not defined
>>> doctest.testmod(loops)
**********************************************************************
File "/home/student/Danya/classwork/loops.py", line 17, in loops.fib1
Failed example:
    fib1(2)
Expected:
    1
Got:
    2
**********************************************************************
File "/home/student/Danya/classwork/loops.py", line 19, in loops.fib1
Failed example:
    fib1(6)
Expected:
    8
Got:
    13
**********************************************************************
1 items had failures:
   2 of   3 in loops.fib1
***Test Failed*** 2 failures.
TestResults(failed=2, attempted=3)
>>> import fibonacci
>>> ================================ RESTART ================================
>>> 
**********************************************************************
File "/home/student/Danya/classwork/fibonacci.py", line 7, in __main__.fib1
Failed example:
    fib1(1)
Expected:
    1
Got nothing
**********************************************************************
File "/home/student/Danya/classwork/fibonacci.py", line 9, in __main__.fib1
Failed example:
    fib1(2)
Expected:
    1
Got nothing
**********************************************************************
File "/home/student/Danya/classwork/fibonacci.py", line 11, in __main__.fib1
Failed example:
    fib1(6)
Expected:
    8
Got nothing
**********************************************************************
File "/home/student/Danya/classwork/fibonacci.py", line 22, in __main__.fib2
Failed example:
    fib2(1)
Expected:
    1
Got nothing
**********************************************************************
File "/home/student/Danya/classwork/fibonacci.py", line 24, in __main__.fib2
Failed example:
    fib2(2)
Expected:
    1
Got nothing
**********************************************************************
File "/home/student/Danya/classwork/fibonacci.py", line 26, in __main__.fib2
Failed example:
    fib2(6)
Expected:
    8
Got nothing
**********************************************************************
2 items had failures:
   3 of   3 in __main__.fib1
   3 of   3 in __main__.fib2
***Test Failed*** 6 failures.
TestResults(failed=6, attempted=6)
>>> ================================ RESTART ================================
>>> 
TestResults(failed=0, attempted=6)
>>> def f(a, b, c):
	return a, b, c

>>> f(1, 2, 3)
(1, 2, 3)
>>> f(a=1, b=2, c=4)
(1, 2, 4)
>>> def f(a, b=1, c=2):
	return a, b, c

>>> f(5)
(5, 1, 2)
>>> f(5, c=5)
(5, 1, 5)
>>> def (a, b, *args):
	
SyntaxError: invalid syntax
>>> def f(a, b, *args):
	return a, b, args

>>> f(1, 2, 3, 4, 5, 6, 7, 8)
(1, 2, (3, 4, 5, 6, 7, 8))
>>> x = [1, 2, 3]
>>> print("hello,", *x)
hello, 1 2 3
>>> print("hello,", 1, 2, 3)
hello, 1 2 3
>>> print("hello,", *x, sep="*")
hello,*1*2*3
>>> def f(a, b, **kwargs):
	return a, b, kwargs

>>> f(1, 2, x=1, y=3)
(1, 2, {'x': 1, 'y': 3})
>>> import random
>>> for line_n in range(5):
	for column_n in range(3):
		print(random.random(), end=",")
	print(random.random())

	
0.44501621531226765,0.8367016375605516,0.4758446623633624,0.4981764728620478
0.0075499312922338024,0.929108901765626,0.20730563237672361,0.12472975072180603
0.9962207278495351,0.4990573178198435,0.16722252520730618,0.4465294879577525
0.3137368365788863,0.9090588136299608,0.36691669634621593,0.4965733854499411
0.556195093713044,0.4391225133679829,0.8290280433243549,0.3732530174879385
>>> for line_n in range(5):
	for column_n in range(3):
		print(random.randint(0, 10), end=",")
	print(random.random())

	
3,5,6,0.7982045188912634
8,10,8,0.19698470252068856
6,0,0,0.2681829729932983
5,0,0,0.12275184124247518
4,2,2,0.6686034212640661
>>> fd = open("example.csv", "w")
>>> for line_n in range(5):
	for column_n in range(3):
		fd.write(str(random.randint(0, 10)) + ",")
	fd.write(str(random.random()) + "\n")

	
2
2
2
21
2
2
2
20
2
2
2
19
2
2
2
18
2
2
2
19
>>> fd.close()
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/student/Danya/classwork/files.py", line 5, in <module>
    str(random.randint(0, 10))
NameError: name 'random' is not defined
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
10
8
4
3
0
>>> ================================ RESTART ================================
>>> 
['2', '5', '7', '0.03183431179431773\n']
['10', '6', '5', '0.08822724815974348\n']
['7', '10', '6', '0.9066947132171451\n']
['10', '8', '7', '0.1286999905085887\n']
['10', '5', '8', '0.15660601722468415\n']
>>> ================================ RESTART ================================
>>> 
['9', '6', '2', '0.28750619234849684']
['8', '8', '3', '0.055923083865566214']
['4', '5', '6', '0.5001537125619994']
['3', '4', '2', '0.9472606633444621']
['3', '2', '3', '0.04571058887253365']
>>> ================================ RESTART ================================
>>> 
75
37
62
21
29
>>> ================================ RESTART ================================
>>> 
75
37
62
21
29
>>> ================================ RESTART ================================
>>> 
12
10
8
3
11
>>> import os
>>> os.getcwd()
'/home/student/Danya/classwork'
>>> import xml
>>> from xml.etree import ElementTree
>>> tree = ElementTree.parse("netlist_5_nodes.xml")
>>> x = tree.findall(".//resistor")
>>> x
[<Element 'resistor' at 0x7f27dc58a278>, <Element 'resistor' at 0x7f27dc58a318>, <Element 'resistor' at 0x7f27dc58a368>, <Element 'resistor' at 0x7f27dc58a3b8>, <Element 'resistor' at 0x7f27dc58a458>, <Element 'resistor' at 0x7f27dc58a4f8>, <Element 'resistor' at 0x7f27dc58a548>, <Element 'resistor' at 0x7f27dc58a5e8>, <Element 'resistor' at 0x7f27dc58a638>, <Element 'resistor' at 0x7f27dc58a6d8>, <Element 'resistor' at 0x7f27dc58a7c8>]
>>> x[0]
<Element 'resistor' at 0x7f27dc58a278>
>>> x[0].attrib
{'net_from': '1', 'resistance': '220.000', 'net_to': '3'}
>>> x[0].text
>>> 
