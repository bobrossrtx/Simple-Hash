# To Convert To JSON
### Text File
When converting a password list to json, you can use a converter to convert the text file into a csv
[Convertio](https://convertio.co/txt-csv/)


### CSV
After converting to a csv, you will get a file called (name).csv. You will want to open up that file in a Text Editor of an IDE to then see the contents that may look like this:
"word"<br>
"word1"<br>
"word2"<br>

###  JSON
Now, you want to make it valid json, so... The best way I can think of is using visual studio codes Find and Replace feature.
So what you want to do is click "CTRL + F". You will see a button that looks like, .*<br>
click that and write in the text box, ("\n) then click the arrow next to the text box looking like, ><br>
Now enter: ", then it will be in a minified list, but you can always ad \n to the end to make a new line for each item.
Now all you have to do is add it into a list.<br>
```json
{
    "words": [
        "word",
        "word1",
        "word2"
    ]
}
```
If your json has a few errors in it, take it to a json validator online and see what the errors are.

<strong>I do not recommend going through password lists like ROCKYOU.txt or any others like them since they are way too big</strong>
