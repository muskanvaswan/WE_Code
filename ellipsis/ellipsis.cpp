#include <iostream>
using namespace std;

string padding = "...";

int getMaxLen(bool isLong) {

    return isLong ? 25 : 10;
}

string addElipsis(string heading) {
    return heading + padding;
}

string ellipsisedString(string heading, bool isLong) {
    int maxLen = getMaxLen(isLong);

    if(heading.length() <= maxLen) {
        return heading;
    }
    

    return addElipsis(heading.substr(0, maxLen - padding.length()));
}

int main(int argc, char* argv[]) {
    cout << ellipsisedString(argv[1], false);
}
