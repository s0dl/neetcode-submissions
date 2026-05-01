class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f"{len(string)}#{string}" for string in strs])
            

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        j = 0
        while i < len(s):
            if s[j] != '#':
                j += 1
                continue

            length = int(s[i:j])
            characters = s[j+1:j+length + 1]

            output.append(characters);

            i = j + length + 1
            j = i

        return output
