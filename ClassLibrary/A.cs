/*
 *  @Author: Mainul (mainul@gmail.com) 
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ClassLibrary
{
    public class A : System.Attribute
    {
        string _name;
        int _id;

        public A(String name, int id) {
            _name = name;
            _id = id;
        }


        public string Name {
            get {
                return _name;
            }

            set {
                _name = value;
            }
        }

        
        public int Id {
            get {
                return _id;
            }

            set {
                _id = value;
            }
        }

    }
}
