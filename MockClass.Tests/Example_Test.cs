using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Microsoft.Pex.Framework;
using Microsoft.Pex.Framework.Using;
using ClassLibrary;
using ClassLibrary.Moles;


namespace MockClass.Tests
{
    [PexClass]
    [TestClass]
    public partial class Example_Test
    {
        [PexMethod]
        [PexAssertReachEventually(0, 1, 2)]
        [PexUseType(typeof(SI)), PexUseType(typeof(SJ)), PexUseType(typeof(SA))]
        [PexUseType(typeof(MA))]
        
        public void foo(I i)
        {
            //i.m1();
            PexAssert.ReachEventually(0);
            //throw new Exception("0");

            if (i is J)
            {
                J j = (J)i;
                //j.m2();
                PexAssert.ReachEventually(1);
                throw new Exception("1");
            }

            if (i.GetType().GetCustomAttributes(true)[0] is A)
            {
                PexAssert.ReachEventually(2);
                throw new Exception("2");
            }
        }
    }
}
