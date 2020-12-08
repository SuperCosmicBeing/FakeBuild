#Let's have some fun lmao
import time
import os
import sys
import cursor
from colorama import Fore, Back, Style 
import random

def lunch():
    #print("Trying dependencies-only mode on a non-existing device tree?")
    #TODO: Make the a variable for codename and switch to latest build id
    lunch = """

============================================
PLATFORM_VERSION_CODENAME=REL
PLATFORM_VERSION=11
DERP_VERSION=11-Official-Alpha-sakura-20201207-1223
TARGET_PRODUCT=derp_sakura
TARGET_BUILD_VARIANT=userdebug
TARGET_ARCH=arm64
TARGET_ARCH_VARIANT=armv8-a
TARGET_CPU_VARIANT=cortex-a53
BUILD_ID=RD1B.201105.010
============================================

    """
    print(lunch)

def ls():
    i = 0
    j = 1
    lslist = [ "\033[39m1script.sh      ",
"Android.bp      ","build           ","\033[39mbootstrap.bash  ","device          ","libnativehelper ","prebuilts       ",
"vendor          ","compatibility   ","external        ","exec            ",
"\033[39mMakefile        ","manifest        ","sdk             ","art             ","cts             ","frameworks      ",
"out             ","system          ",
"bionic          ","dalvik          ","hardware        ","packages        ","test            ",
"bootable        ","developers      ","kernel          ","pdk             ","toolchain       ",
"development     ","libcore         ","platform_testing","tools           "
    ]
    while i <= 29:
        print(Fore.BLUE + lslist[i],"  ",lslist[j]) 
        i += 2
        j += 2
    print(Style.RESET_ALL)

def make():
    cursor.hide()
    c = "/data/data/com.termux/files/home/derp/out/.bootstrap/"
    p = ["link","cc","compile","gotestmain"]
    #These strings might not really exist lmao
    clist = [ "blueprint-parser/pkg/github.com/google/blueprint/parser.a",
              "blueprint-gotestmain/pkg/github.com/google/blueprint/gotestmain.a",
              "proptools-blueprint/pkg/github.com/google/blueprint/proptools.a",
              "blueprint/test/pkg/github.com/blueprint/blueprint.a",
              "gotostmain/github.com/pkg/a.out",
              "blueprint-bootstrap-bpdoc/test/pkg/github.com/blueprint/blueprint.a",
              "blueprint/test/test",
              "blueprint-test/test/blueprint/test.a",
              "blueprint-parser/test/test",
              "blueprint-proptools/test/test.a",
              "gostunner-test/obj/gostunner.a",
              "gostunner/obj/a.out",
              "gostunner/minibp/obj/a.out",
              "blueprint/gocest-main.a",
              "minibootstrap/build.ninja.a"
            ]
            
    i = 1
    tim = 0
    ti = 1
    RED="\033[1;31m" 
    YELLOW="\033[1;33m"
    NC="\033[0m"
    
    while i <= 63:
        os.system("clear")
        lunch()
        crl = c+random.choice(clist)
        print("[{0}/64] {1}: {2}".format(i,random.choice(p),crl))
        i += 1
        tm = random.random()
        time.sleep(tm)
    while True:
        try:
            os.system("clear")
            lunch()
            print("[64/64] out/soong/.bootstrap/bin/soong_build out/soong/build.ninja")
            if ti <= 20:        
                print("       {0}:{1} out/soong/.bootstrap/bin/soong_build out/soong/build.ninja".format(tim,ti))
            elif ti > 20 and tim < 1 and ti <= 30:
                print("       {0}{1}:{2}{3} out/soong/.bootstrap/bin/soong_build out/soong/build.ninja".format(YELLOW,tim,ti,NC))
            elif ti > 30 or ti >= 1 and ti <= 60:
                print("       {0}{1}:{2}{3} out/soong/.bootstrap/bin/soong_build out/soong/build.ninja".format(RED,tim,ti,NC))
            elif ti == 60:
                ti = 0
                tim += 1
            time.sleep(1)
            ti += 1
        except KeyboardInterrupt:
            print("\n",RED,"Received Signal Interrupt",NC)
            time.sleep(1)
            print(RED,"Ninja failed with: exit status 1",NC)
            cursor.show()
            sys.exit()
            
#Lets Finalize
while True:
    inp = input("$ ")
    inps = inp.split()
    inps1 = inps[0]
    if inps1 == "lunch":
        time.sleep(5)
        print("Trying dependencies-only mode on a non-existing device tree?")
        time.sleep(1)
        lunch()
    elif inps1 == "mka":
    	time.sleep(0.8)
    	make()
    elif inps1 == "neofetch":
        os.system("neofetch")
    elif inps1 == "clear":
        os.system("clear")
    elif inps1 == "exit":
        sys.exit()
    elif inps1 == "ls":
    	ls()
    elif inps1 == "cd":
    	None
    elif inps1 == "whoami":
        print("u0_a316")
    elif inps1 == "." or inps1 == "source":
        time.sleep(1.8)
        print("ccache found and CCACHE_EXEC has been set to : /data/data/com.termux/files/usr/bin/ccache")
    else:
    	print(inps1,": command not found")
