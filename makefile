encode: Encode.class
	@java Encode $(ARGS)
Encode.class: Encode.java
	@javac Encode.java
decode: 
	@python3 decode.py decode $(ARGS)
clean:
	rm *.class
