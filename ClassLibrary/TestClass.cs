/*
 *  @Author: Mainul (mainul@gmail.com) 
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ClassLibrary
{
    class TestClass
    {
        public void foo(I i) {

            i.m1(); 
            // goal 0

            if (i is J) {
                J j = (J) i; 
                // goal 1

                if (i.GetType().GetCustomAttributes(true)[0] is A) { 
                    // goal 2
                }
            }
        }

    }
}
