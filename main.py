def replace_word_in_file(file_path, target_word, replacement_word):
    with open(file_path, 'r+') as file:
        content = file.read()
        modified_content = content.replace(target_word, replacement_word)
        file.seek(0)
        file.write(modified_content)
        file.truncate()
# the function abouve replaces a keyword to the word you want.
def copy_lines(lookup_file, selected_lines, output_file):
    with open(lookup_file, 'r') as lookup_file:
        lookup_table = lookup_file.readlines()

    with open(output_file, 'w') as output_file:
        for line_number in selected_lines:
            try:
                line_to_copy = lookup_table[line_number] #.strip()
                output_file.write(line_to_copy + '\n')
            except IndexError:
                print(f"Line number {line_number} does not exist in the lookup table.")
# the function abouve will take the lookup table and put lines you want to a c++ file that is created at runtime.

print("version 0.1 (prototype)")
print("Hello this program was created by chikenbob")

selected_lines = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153] # im sorry i will try to make it more clean later

element_name = input("what do you want your element to be called: ")

lookup_file = 'lookup_table.txt'
output_file = element_name + '.c++'
target_word = 'edit'

copy_lines(lookup_file, selected_lines, output_file)
replace_word_in_file(output_file, target_word, element_name) #what you can do is add more replace_word_in_file() to add more varibles