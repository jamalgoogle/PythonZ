def build_compression_index(input_string):
   if not input_string:
      return ""
   
   index = []
   count = 1
   current_char = input_string[0]

   for char in input_string[1:]:
      if char == current_char:
         count += 1
      else:
         index.append((current_char, count))
         current_char = char
         count = 1

   index.append((current_char, count))

   compressedTxt = ''.join(f"{char}{count}" for char, count in index)
   return compressedTxt if len(compressedTxt) < len(input_string) else input_string


input_string = "AABBBCCCC"
compressedTxt = build_compression_index(input_string)
print(compressedTxt)




   