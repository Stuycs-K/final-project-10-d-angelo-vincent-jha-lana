encode: Encode.class
	@java Encode $(ARGS)
Encode.class: Encode.java
	@javac Encode.java
clean:
	@rm *.class
