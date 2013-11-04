# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 proto_parser.g 2013-10-23 04:20:56

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EXPONENT=60
MESSAGE_LITERAL=11
REQUIRED_PROTOBUF_SCOPE_LITERAL=29
STRING_GUTS=54
EQUALS=25
UINT32_PROTOBUF_TYPE_LITERAL=37
INT32_PROTOBUF_TYPE_LITERAL=35
EOF=-1
UINT64_PROTOBUF_TYPE_LITERAL=38
ENUM_FIELD=70
ESCAPE_SEQUENCE=56
QUALIFIED_IDENTIFIER=63
FIXED64_PROTOBUF_TYPE_LITERAL=42
UNICODE_ESCAPE=58
STRING_LITERAL=55
FIXED32_PROTOBUF_TYPE_LITERAL=41
PACKAGE_LITERAL=7
COMMA=27
OPTION_CUSTOMIZED=67
IDENTIFIER=62
EXTEND_LITERAL=12
REPEATED_PROTOBUF_SCOPE_LITERAL=31
PROTOBUF_TYPE_LITERAL=48
OPTION_VALUE_ITEM=68
ENUM_LITERAL=10
IMPORT_LITERAL=8
HEX_LITERAL=49
COMMENT=5
FLOAT_PROTOBUF_TYPE_LITERAL=34
BYTES_PROTOBUF_TYPE_LITERAL=47
BLOCK_OPEN=19
SFIXED64_PROTOBUF_TYPE_LITERAL=44
SERVICE_LITERAL=16
PROTOBUF_SCOPE_LITERAL=32
MESSAGE_FIELD=71
END_OF_LINE=4
EXTENSIONS_TO_LITERAL=14
OPTIONAL_PROTOBUF_SCOPE_LITERAL=30
PAREN_CLOSE=22
BOOL_PROTOBUF_TYPE_LITERAL=45
ITEM_TERMINATOR=28
OPTION_VALUE_OBJECT=69
OCTAL_LITERAL=50
EXTENSIONS_MAX_LITERAL=15
OPTION_LITERAL=9
WHITESPACE=6
STRING_PROTOBUF_TYPE_LITERAL=46
HEX_DIGIT=53
OCTAL_ESCAPE=57
BOOL_LITERAL=59
EXTENSIONS_DEF_LITERAL=13
SINT32_PROTOBUF_TYPE_LITERAL=39
COLON=26
FLOAT_LITERAL=61
INT64_PROTOBUF_TYPE_LITERAL=36
BLOCK_CLOSE=20
FIELD_IDENTIFIER=64
INTEGER_LITERAL=52
OPTION_PREDEFINED=66
PAREN_OPEN=21
SFIXED32_PROTOBUF_TYPE_LITERAL=43
DOUBLE_PROTOBUF_TYPE_LITERAL=33
PROTO=65
DECIMAL_LITERAL=51
SINT64_PROTOBUF_TYPE_LITERAL=40
BRACKET_CLOSE=24
RPC_LITERAL=18
BRACKET_OPEN=23
RETURNS_LITERAL=17

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "END_OF_LINE", "COMMENT", "WHITESPACE", "PACKAGE_LITERAL", "IMPORT_LITERAL", 
    "OPTION_LITERAL", "ENUM_LITERAL", "MESSAGE_LITERAL", "EXTEND_LITERAL", 
    "EXTENSIONS_DEF_LITERAL", "EXTENSIONS_TO_LITERAL", "EXTENSIONS_MAX_LITERAL", 
    "SERVICE_LITERAL", "RETURNS_LITERAL", "RPC_LITERAL", "BLOCK_OPEN", "BLOCK_CLOSE", 
    "PAREN_OPEN", "PAREN_CLOSE", "BRACKET_OPEN", "BRACKET_CLOSE", "EQUALS", 
    "COLON", "COMMA", "ITEM_TERMINATOR", "REQUIRED_PROTOBUF_SCOPE_LITERAL", 
    "OPTIONAL_PROTOBUF_SCOPE_LITERAL", "REPEATED_PROTOBUF_SCOPE_LITERAL", 
    "PROTOBUF_SCOPE_LITERAL", "DOUBLE_PROTOBUF_TYPE_LITERAL", "FLOAT_PROTOBUF_TYPE_LITERAL", 
    "INT32_PROTOBUF_TYPE_LITERAL", "INT64_PROTOBUF_TYPE_LITERAL", "UINT32_PROTOBUF_TYPE_LITERAL", 
    "UINT64_PROTOBUF_TYPE_LITERAL", "SINT32_PROTOBUF_TYPE_LITERAL", "SINT64_PROTOBUF_TYPE_LITERAL", 
    "FIXED32_PROTOBUF_TYPE_LITERAL", "FIXED64_PROTOBUF_TYPE_LITERAL", "SFIXED32_PROTOBUF_TYPE_LITERAL", 
    "SFIXED64_PROTOBUF_TYPE_LITERAL", "BOOL_PROTOBUF_TYPE_LITERAL", "STRING_PROTOBUF_TYPE_LITERAL", 
    "BYTES_PROTOBUF_TYPE_LITERAL", "PROTOBUF_TYPE_LITERAL", "HEX_LITERAL", 
    "OCTAL_LITERAL", "DECIMAL_LITERAL", "INTEGER_LITERAL", "HEX_DIGIT", 
    "STRING_GUTS", "STRING_LITERAL", "ESCAPE_SEQUENCE", "OCTAL_ESCAPE", 
    "UNICODE_ESCAPE", "BOOL_LITERAL", "EXPONENT", "FLOAT_LITERAL", "IDENTIFIER", 
    "QUALIFIED_IDENTIFIER", "FIELD_IDENTIFIER", "PROTO", "OPTION_PREDEFINED", 
    "OPTION_CUSTOMIZED", "OPTION_VALUE_ITEM", "OPTION_VALUE_OBJECT", "ENUM_FIELD", 
    "MESSAGE_FIELD"
]




class proto_parser(Parser):
    grammarFileName = "proto_parser.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(proto_parser, self).__init__(input, state, *args, **kwargs)






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class all_identifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.all_identifier_return, self).__init__()

            self.tree = None




    # $ANTLR start "all_identifier"
    # proto_parser.g:22:1: all_identifier : ( IDENTIFIER | QUALIFIED_IDENTIFIER );
    def all_identifier(self, ):

        retval = self.all_identifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set1 = None

        set1_tree = None

        try:
            try:
                # proto_parser.g:23:3: ( IDENTIFIER | QUALIFIED_IDENTIFIER )
                # proto_parser.g:
                pass 
                root_0 = self._adaptor.nil()

                set1 = self.input.LT(1)
                if (IDENTIFIER <= self.input.LA(1) <= QUALIFIED_IDENTIFIER):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set1))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "all_identifier"

    class all_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.all_value_return, self).__init__()

            self.tree = None




    # $ANTLR start "all_value"
    # proto_parser.g:27:1: all_value : ( IDENTIFIER | literal_value );
    def all_value(self, ):

        retval = self.all_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER2 = None
        literal_value3 = None


        IDENTIFIER2_tree = None

        try:
            try:
                # proto_parser.g:28:3: ( IDENTIFIER | literal_value )
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == IDENTIFIER) :
                    alt1 = 1
                elif (LA1_0 == INTEGER_LITERAL or LA1_0 == STRING_LITERAL or LA1_0 == BOOL_LITERAL or LA1_0 == FLOAT_LITERAL) :
                    alt1 = 2
                else:
                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae

                if alt1 == 1:
                    # proto_parser.g:28:6: IDENTIFIER
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENTIFIER2=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_all_value129)

                    IDENTIFIER2_tree = self._adaptor.createWithPayload(IDENTIFIER2)
                    self._adaptor.addChild(root_0, IDENTIFIER2_tree)



                elif alt1 == 2:
                    # proto_parser.g:29:6: literal_value
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_literal_value_in_all_value136)
                    literal_value3 = self.literal_value()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, literal_value3.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "all_value"

    class literal_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.literal_value_return, self).__init__()

            self.tree = None




    # $ANTLR start "literal_value"
    # proto_parser.g:32:1: literal_value : ( INTEGER_LITERAL | STRING_LITERAL | BOOL_LITERAL | FLOAT_LITERAL );
    def literal_value(self, ):

        retval = self.literal_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set4 = None

        set4_tree = None

        try:
            try:
                # proto_parser.g:33:3: ( INTEGER_LITERAL | STRING_LITERAL | BOOL_LITERAL | FLOAT_LITERAL )
                # proto_parser.g:
                pass 
                root_0 = self._adaptor.nil()

                set4 = self.input.LT(1)
                if self.input.LA(1) == INTEGER_LITERAL or self.input.LA(1) == STRING_LITERAL or self.input.LA(1) == BOOL_LITERAL or self.input.LA(1) == FLOAT_LITERAL:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set4))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "literal_value"

    class proto_type_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.proto_type_return, self).__init__()

            self.tree = None




    # $ANTLR start "proto_type"
    # proto_parser.g:39:1: proto_type : ( PROTOBUF_TYPE_LITERAL | all_identifier );
    def proto_type(self, ):

        retval = self.proto_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PROTOBUF_TYPE_LITERAL5 = None
        all_identifier6 = None


        PROTOBUF_TYPE_LITERAL5_tree = None

        try:
            try:
                # proto_parser.g:40:3: ( PROTOBUF_TYPE_LITERAL | all_identifier )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == PROTOBUF_TYPE_LITERAL) :
                    alt2 = 1
                elif ((IDENTIFIER <= LA2_0 <= QUALIFIED_IDENTIFIER)) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # proto_parser.g:40:6: PROTOBUF_TYPE_LITERAL
                    pass 
                    root_0 = self._adaptor.nil()

                    PROTOBUF_TYPE_LITERAL5=self.match(self.input, PROTOBUF_TYPE_LITERAL, self.FOLLOW_PROTOBUF_TYPE_LITERAL_in_proto_type185)

                    PROTOBUF_TYPE_LITERAL5_tree = self._adaptor.createWithPayload(PROTOBUF_TYPE_LITERAL5)
                    self._adaptor.addChild(root_0, PROTOBUF_TYPE_LITERAL5_tree)



                elif alt2 == 2:
                    # proto_parser.g:41:6: all_identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_all_identifier_in_proto_type192)
                    all_identifier6 = self.all_identifier()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, all_identifier6.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "proto_type"

    class proto_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.proto_return, self).__init__()

            self.tree = None




    # $ANTLR start "proto"
    # proto_parser.g:45:1: proto : ( package_def | import_def | option_line_def | enum_def | ext_def | message_def | service_def )* EOF -> ^( PROTO ( package_def )* ( import_def )* ( option_line_def )* ( enum_def )* ( ext_def )* ( message_def )* ( service_def )* ) ;
    def proto(self, ):

        retval = self.proto_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF14 = None
        package_def7 = None

        import_def8 = None

        option_line_def9 = None

        enum_def10 = None

        ext_def11 = None

        message_def12 = None

        service_def13 = None


        EOF14_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_enum_def = RewriteRuleSubtreeStream(self._adaptor, "rule enum_def")
        stream_message_def = RewriteRuleSubtreeStream(self._adaptor, "rule message_def")
        stream_import_def = RewriteRuleSubtreeStream(self._adaptor, "rule import_def")
        stream_service_def = RewriteRuleSubtreeStream(self._adaptor, "rule service_def")
        stream_ext_def = RewriteRuleSubtreeStream(self._adaptor, "rule ext_def")
        stream_option_line_def = RewriteRuleSubtreeStream(self._adaptor, "rule option_line_def")
        stream_package_def = RewriteRuleSubtreeStream(self._adaptor, "rule package_def")
        try:
            try:
                # proto_parser.g:46:3: ( ( package_def | import_def | option_line_def | enum_def | ext_def | message_def | service_def )* EOF -> ^( PROTO ( package_def )* ( import_def )* ( option_line_def )* ( enum_def )* ( ext_def )* ( message_def )* ( service_def )* ) )
                # proto_parser.g:46:6: ( package_def | import_def | option_line_def | enum_def | ext_def | message_def | service_def )* EOF
                pass 
                # proto_parser.g:46:6: ( package_def | import_def | option_line_def | enum_def | ext_def | message_def | service_def )*
                while True: #loop3
                    alt3 = 8
                    LA3 = self.input.LA(1)
                    if LA3 == PACKAGE_LITERAL:
                        alt3 = 1
                    elif LA3 == IMPORT_LITERAL:
                        alt3 = 2
                    elif LA3 == OPTION_LITERAL:
                        alt3 = 3
                    elif LA3 == ENUM_LITERAL:
                        alt3 = 4
                    elif LA3 == EXTEND_LITERAL:
                        alt3 = 5
                    elif LA3 == MESSAGE_LITERAL:
                        alt3 = 6
                    elif LA3 == SERVICE_LITERAL:
                        alt3 = 7

                    if alt3 == 1:
                        # proto_parser.g:46:7: package_def
                        pass 
                        self._state.following.append(self.FOLLOW_package_def_in_proto208)
                        package_def7 = self.package_def()

                        self._state.following.pop()
                        stream_package_def.add(package_def7.tree)


                    elif alt3 == 2:
                        # proto_parser.g:46:21: import_def
                        pass 
                        self._state.following.append(self.FOLLOW_import_def_in_proto212)
                        import_def8 = self.import_def()

                        self._state.following.pop()
                        stream_import_def.add(import_def8.tree)


                    elif alt3 == 3:
                        # proto_parser.g:46:34: option_line_def
                        pass 
                        self._state.following.append(self.FOLLOW_option_line_def_in_proto216)
                        option_line_def9 = self.option_line_def()

                        self._state.following.pop()
                        stream_option_line_def.add(option_line_def9.tree)


                    elif alt3 == 4:
                        # proto_parser.g:46:52: enum_def
                        pass 
                        self._state.following.append(self.FOLLOW_enum_def_in_proto220)
                        enum_def10 = self.enum_def()

                        self._state.following.pop()
                        stream_enum_def.add(enum_def10.tree)


                    elif alt3 == 5:
                        # proto_parser.g:46:63: ext_def
                        pass 
                        self._state.following.append(self.FOLLOW_ext_def_in_proto224)
                        ext_def11 = self.ext_def()

                        self._state.following.pop()
                        stream_ext_def.add(ext_def11.tree)


                    elif alt3 == 6:
                        # proto_parser.g:46:73: message_def
                        pass 
                        self._state.following.append(self.FOLLOW_message_def_in_proto228)
                        message_def12 = self.message_def()

                        self._state.following.pop()
                        stream_message_def.add(message_def12.tree)


                    elif alt3 == 7:
                        # proto_parser.g:46:87: service_def
                        pass 
                        self._state.following.append(self.FOLLOW_service_def_in_proto232)
                        service_def13 = self.service_def()

                        self._state.following.pop()
                        stream_service_def.add(service_def13.tree)


                    else:
                        break #loop3
                EOF14=self.match(self.input, EOF, self.FOLLOW_EOF_in_proto236) 
                stream_EOF.add(EOF14)

                # AST Rewrite
                # elements: service_def, enum_def, message_def, import_def, option_line_def, ext_def, package_def
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 47:6: -> ^( PROTO ( package_def )* ( import_def )* ( option_line_def )* ( enum_def )* ( ext_def )* ( message_def )* ( service_def )* )
                # proto_parser.g:47:9: ^( PROTO ( package_def )* ( import_def )* ( option_line_def )* ( enum_def )* ( ext_def )* ( message_def )* ( service_def )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROTO, "PROTO"), root_1)

                # proto_parser.g:47:17: ( package_def )*
                while stream_package_def.hasNext():
                    self._adaptor.addChild(root_1, stream_package_def.nextTree())


                stream_package_def.reset();
                # proto_parser.g:47:30: ( import_def )*
                while stream_import_def.hasNext():
                    self._adaptor.addChild(root_1, stream_import_def.nextTree())


                stream_import_def.reset();
                # proto_parser.g:47:42: ( option_line_def )*
                while stream_option_line_def.hasNext():
                    self._adaptor.addChild(root_1, stream_option_line_def.nextTree())


                stream_option_line_def.reset();
                # proto_parser.g:47:59: ( enum_def )*
                while stream_enum_def.hasNext():
                    self._adaptor.addChild(root_1, stream_enum_def.nextTree())


                stream_enum_def.reset();
                # proto_parser.g:47:69: ( ext_def )*
                while stream_ext_def.hasNext():
                    self._adaptor.addChild(root_1, stream_ext_def.nextTree())


                stream_ext_def.reset();
                # proto_parser.g:47:78: ( message_def )*
                while stream_message_def.hasNext():
                    self._adaptor.addChild(root_1, stream_message_def.nextTree())


                stream_message_def.reset();
                # proto_parser.g:47:91: ( service_def )*
                while stream_service_def.hasNext():
                    self._adaptor.addChild(root_1, stream_service_def.nextTree())


                stream_service_def.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "proto"

    class package_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.package_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "package_def"
    # proto_parser.g:52:1: package_def : PACKAGE_LITERAL package_name ITEM_TERMINATOR -> ^( PACKAGE_LITERAL package_name ) ;
    def package_def(self, ):

        retval = self.package_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PACKAGE_LITERAL15 = None
        ITEM_TERMINATOR17 = None
        package_name16 = None


        PACKAGE_LITERAL15_tree = None
        ITEM_TERMINATOR17_tree = None
        stream_PACKAGE_LITERAL = RewriteRuleTokenStream(self._adaptor, "token PACKAGE_LITERAL")
        stream_ITEM_TERMINATOR = RewriteRuleTokenStream(self._adaptor, "token ITEM_TERMINATOR")
        stream_package_name = RewriteRuleSubtreeStream(self._adaptor, "rule package_name")
        try:
            try:
                # proto_parser.g:53:3: ( PACKAGE_LITERAL package_name ITEM_TERMINATOR -> ^( PACKAGE_LITERAL package_name ) )
                # proto_parser.g:53:6: PACKAGE_LITERAL package_name ITEM_TERMINATOR
                pass 
                PACKAGE_LITERAL15=self.match(self.input, PACKAGE_LITERAL, self.FOLLOW_PACKAGE_LITERAL_in_package_def286) 
                stream_PACKAGE_LITERAL.add(PACKAGE_LITERAL15)
                self._state.following.append(self.FOLLOW_package_name_in_package_def288)
                package_name16 = self.package_name()

                self._state.following.pop()
                stream_package_name.add(package_name16.tree)
                ITEM_TERMINATOR17=self.match(self.input, ITEM_TERMINATOR, self.FOLLOW_ITEM_TERMINATOR_in_package_def290) 
                stream_ITEM_TERMINATOR.add(ITEM_TERMINATOR17)

                # AST Rewrite
                # elements: PACKAGE_LITERAL, package_name
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 54:6: -> ^( PACKAGE_LITERAL package_name )
                # proto_parser.g:54:9: ^( PACKAGE_LITERAL package_name )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_PACKAGE_LITERAL.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_package_name.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "package_def"

    class package_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.package_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "package_name"
    # proto_parser.g:57:1: package_name : all_identifier ;
    def package_name(self, ):

        retval = self.package_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        all_identifier18 = None



        try:
            try:
                # proto_parser.g:57:14: ( all_identifier )
                # proto_parser.g:57:16: all_identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_all_identifier_in_package_name314)
                all_identifier18 = self.all_identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, all_identifier18.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "package_name"

    class import_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.import_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "import_def"
    # proto_parser.g:61:1: import_def : IMPORT_LITERAL import_file_name ITEM_TERMINATOR -> ^( IMPORT_LITERAL import_file_name ) ;
    def import_def(self, ):

        retval = self.import_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORT_LITERAL19 = None
        ITEM_TERMINATOR21 = None
        import_file_name20 = None


        IMPORT_LITERAL19_tree = None
        ITEM_TERMINATOR21_tree = None
        stream_IMPORT_LITERAL = RewriteRuleTokenStream(self._adaptor, "token IMPORT_LITERAL")
        stream_ITEM_TERMINATOR = RewriteRuleTokenStream(self._adaptor, "token ITEM_TERMINATOR")
        stream_import_file_name = RewriteRuleSubtreeStream(self._adaptor, "rule import_file_name")
        try:
            try:
                # proto_parser.g:62:3: ( IMPORT_LITERAL import_file_name ITEM_TERMINATOR -> ^( IMPORT_LITERAL import_file_name ) )
                # proto_parser.g:62:6: IMPORT_LITERAL import_file_name ITEM_TERMINATOR
                pass 
                IMPORT_LITERAL19=self.match(self.input, IMPORT_LITERAL, self.FOLLOW_IMPORT_LITERAL_in_import_def328) 
                stream_IMPORT_LITERAL.add(IMPORT_LITERAL19)
                self._state.following.append(self.FOLLOW_import_file_name_in_import_def330)
                import_file_name20 = self.import_file_name()

                self._state.following.pop()
                stream_import_file_name.add(import_file_name20.tree)
                ITEM_TERMINATOR21=self.match(self.input, ITEM_TERMINATOR, self.FOLLOW_ITEM_TERMINATOR_in_import_def332) 
                stream_ITEM_TERMINATOR.add(ITEM_TERMINATOR21)

                # AST Rewrite
                # elements: import_file_name, IMPORT_LITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 63:6: -> ^( IMPORT_LITERAL import_file_name )
                # proto_parser.g:63:9: ^( IMPORT_LITERAL import_file_name )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_IMPORT_LITERAL.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_import_file_name.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "import_def"

    class import_file_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.import_file_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "import_file_name"
    # proto_parser.g:66:1: import_file_name : STRING_LITERAL ;
    def import_file_name(self, ):

        retval = self.import_file_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STRING_LITERAL22 = None

        STRING_LITERAL22_tree = None

        try:
            try:
                # proto_parser.g:66:18: ( STRING_LITERAL )
                # proto_parser.g:66:20: STRING_LITERAL
                pass 
                root_0 = self._adaptor.nil()

                STRING_LITERAL22=self.match(self.input, STRING_LITERAL, self.FOLLOW_STRING_LITERAL_in_import_file_name356)

                STRING_LITERAL22_tree = self._adaptor.createWithPayload(STRING_LITERAL22)
                self._adaptor.addChild(root_0, STRING_LITERAL22_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "import_file_name"

    class option_line_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.option_line_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "option_line_def"
    # proto_parser.g:70:1: option_line_def : OPTION_LITERAL option_name EQUALS option_all_value ITEM_TERMINATOR -> ^( OPTION_LITERAL option_name option_all_value ) ;
    def option_line_def(self, ):

        retval = self.option_line_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPTION_LITERAL23 = None
        EQUALS25 = None
        ITEM_TERMINATOR27 = None
        option_name24 = None

        option_all_value26 = None


        OPTION_LITERAL23_tree = None
        EQUALS25_tree = None
        ITEM_TERMINATOR27_tree = None
        stream_OPTION_LITERAL = RewriteRuleTokenStream(self._adaptor, "token OPTION_LITERAL")
        stream_EQUALS = RewriteRuleTokenStream(self._adaptor, "token EQUALS")
        stream_ITEM_TERMINATOR = RewriteRuleTokenStream(self._adaptor, "token ITEM_TERMINATOR")
        stream_option_name = RewriteRuleSubtreeStream(self._adaptor, "rule option_name")
        stream_option_all_value = RewriteRuleSubtreeStream(self._adaptor, "rule option_all_value")
        try:
            try:
                # proto_parser.g:71:3: ( OPTION_LITERAL option_name EQUALS option_all_value ITEM_TERMINATOR -> ^( OPTION_LITERAL option_name option_all_value ) )
                # proto_parser.g:71:6: OPTION_LITERAL option_name EQUALS option_all_value ITEM_TERMINATOR
                pass 
                OPTION_LITERAL23=self.match(self.input, OPTION_LITERAL, self.FOLLOW_OPTION_LITERAL_in_option_line_def370) 
                stream_OPTION_LITERAL.add(OPTION_LITERAL23)
                self._state.following.append(self.FOLLOW_option_name_in_option_line_def372)
                option_name24 = self.option_name()

                self._state.following.pop()
                stream_option_name.add(option_name24.tree)
                EQUALS25=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_option_line_def374) 
                stream_EQUALS.add(EQUALS25)
                self._state.following.append(self.FOLLOW_option_all_value_in_option_line_def376)
                option_all_value26 = self.option_all_value()

                self._state.following.pop()
                stream_option_all_value.add(option_all_value26.tree)
                ITEM_TERMINATOR27=self.match(self.input, ITEM_TERMINATOR, self.FOLLOW_ITEM_TERMINATOR_in_option_line_def378) 
                stream_ITEM_TERMINATOR.add(ITEM_TERMINATOR27)

                # AST Rewrite
                # elements: OPTION_LITERAL, option_name, option_all_value
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 72:6: -> ^( OPTION_LITERAL option_name option_all_value )
                # proto_parser.g:72:9: ^( OPTION_LITERAL option_name option_all_value )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_OPTION_LITERAL.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_option_name.nextTree())
                self._adaptor.addChild(root_1, stream_option_all_value.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "option_line_def"

    class option_field_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.option_field_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "option_field_def"
    # proto_parser.g:75:1: option_field_def : BRACKET_OPEN option_field_item ( COMMA option_field_item )* BRACKET_CLOSE ;
    def option_field_def(self, ):

        retval = self.option_field_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BRACKET_OPEN28 = None
        COMMA30 = None
        BRACKET_CLOSE32 = None
        option_field_item29 = None

        option_field_item31 = None


        BRACKET_OPEN28_tree = None
        COMMA30_tree = None
        BRACKET_CLOSE32_tree = None

        try:
            try:
                # proto_parser.g:76:3: ( BRACKET_OPEN option_field_item ( COMMA option_field_item )* BRACKET_CLOSE )
                # proto_parser.g:76:6: BRACKET_OPEN option_field_item ( COMMA option_field_item )* BRACKET_CLOSE
                pass 
                root_0 = self._adaptor.nil()

                BRACKET_OPEN28=self.match(self.input, BRACKET_OPEN, self.FOLLOW_BRACKET_OPEN_in_option_field_def407)
                self._state.following.append(self.FOLLOW_option_field_item_in_option_field_def410)
                option_field_item29 = self.option_field_item()

                self._state.following.pop()
                self._adaptor.addChild(root_0, option_field_item29.tree)
                # proto_parser.g:76:38: ( COMMA option_field_item )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == COMMA) :
                        alt4 = 1


                    if alt4 == 1:
                        # proto_parser.g:76:39: COMMA option_field_item
                        pass 
                        COMMA30=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_option_field_def413)
                        self._state.following.append(self.FOLLOW_option_field_item_in_option_field_def416)
                        option_field_item31 = self.option_field_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, option_field_item31.tree)


                    else:
                        break #loop4
                BRACKET_CLOSE32=self.match(self.input, BRACKET_CLOSE, self.FOLLOW_BRACKET_CLOSE_in_option_field_def420)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "option_field_def"

    class option_field_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.option_field_item_return, self).__init__()

            self.tree = None




    # $ANTLR start "option_field_item"
    # proto_parser.g:79:1: option_field_item : option_name EQUALS option_all_value -> ^( OPTION_LITERAL option_name option_all_value ) ;
    def option_field_item(self, ):

        retval = self.option_field_item_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQUALS34 = None
        option_name33 = None

        option_all_value35 = None


        EQUALS34_tree = None
        stream_EQUALS = RewriteRuleTokenStream(self._adaptor, "token EQUALS")
        stream_option_name = RewriteRuleSubtreeStream(self._adaptor, "rule option_name")
        stream_option_all_value = RewriteRuleSubtreeStream(self._adaptor, "rule option_all_value")
        try:
            try:
                # proto_parser.g:80:3: ( option_name EQUALS option_all_value -> ^( OPTION_LITERAL option_name option_all_value ) )
                # proto_parser.g:80:6: option_name EQUALS option_all_value
                pass 
                self._state.following.append(self.FOLLOW_option_name_in_option_field_item435)
                option_name33 = self.option_name()

                self._state.following.pop()
                stream_option_name.add(option_name33.tree)
                EQUALS34=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_option_field_item437) 
                stream_EQUALS.add(EQUALS34)
                self._state.following.append(self.FOLLOW_option_all_value_in_option_field_item439)
                option_all_value35 = self.option_all_value()

                self._state.following.pop()
                stream_option_all_value.add(option_all_value35.tree)

                # AST Rewrite
                # elements: option_all_value, option_name
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 81:6: -> ^( OPTION_LITERAL option_name option_all_value )
                # proto_parser.g:81:9: ^( OPTION_LITERAL option_name option_all_value )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTION_LITERAL, "OPTION_LITERAL"), root_1)

                self._adaptor.addChild(root_1, stream_option_name.nextTree())
                self._adaptor.addChild(root_1, stream_option_all_value.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "option_field_item"

    class option_all_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.option_all_value_return, self).__init__()

            self.tree = None




    # $ANTLR start "option_all_value"
    # proto_parser.g:84:1: option_all_value : ( all_value | option_value_object );
    def option_all_value(self, ):

        retval = self.option_all_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        all_value36 = None

        option_value_object37 = None



        try:
            try:
                # proto_parser.g:85:3: ( all_value | option_value_object )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == INTEGER_LITERAL or LA5_0 == STRING_LITERAL or LA5_0 == BOOL_LITERAL or (FLOAT_LITERAL <= LA5_0 <= IDENTIFIER)) :
                    alt5 = 1
                elif (LA5_0 == BLOCK_OPEN) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # proto_parser.g:85:5: all_value
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_all_value_in_option_all_value467)
                    all_value36 = self.all_value()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, all_value36.tree)


                elif alt5 == 2:
                    # proto_parser.g:86:5: option_value_object
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_option_value_object_in_option_all_value473)
                    option_value_object37 = self.option_value_object()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, option_value_object37.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "option_all_value"

    class option_value_object_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.option_value_object_return, self).__init__()

            self.tree = None




    # $ANTLR start "option_value_object"
    # proto_parser.g:89:1: option_value_object : BLOCK_OPEN ( option_value_item )* BLOCK_CLOSE -> ^( OPTION_VALUE_OBJECT ( option_value_item )* ) ;
    def option_value_object(self, ):

        retval = self.option_value_object_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BLOCK_OPEN38 = None
        BLOCK_CLOSE40 = None
        option_value_item39 = None


        BLOCK_OPEN38_tree = None
        BLOCK_CLOSE40_tree = None
        stream_BLOCK_OPEN = RewriteRuleTokenStream(self._adaptor, "token BLOCK_OPEN")
        stream_BLOCK_CLOSE = RewriteRuleTokenStream(self._adaptor, "token BLOCK_CLOSE")
        stream_option_value_item = RewriteRuleSubtreeStream(self._adaptor, "rule option_value_item")
        try:
            try:
                # proto_parser.g:90:3: ( BLOCK_OPEN ( option_value_item )* BLOCK_CLOSE -> ^( OPTION_VALUE_OBJECT ( option_value_item )* ) )
                # proto_parser.g:90:6: BLOCK_OPEN ( option_value_item )* BLOCK_CLOSE
                pass 
                BLOCK_OPEN38=self.match(self.input, BLOCK_OPEN, self.FOLLOW_BLOCK_OPEN_in_option_value_object487) 
                stream_BLOCK_OPEN.add(BLOCK_OPEN38)
                # proto_parser.g:90:17: ( option_value_item )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == IDENTIFIER) :
                        alt6 = 1


                    if alt6 == 1:
                        # proto_parser.g:90:17: option_value_item
                        pass 
                        self._state.following.append(self.FOLLOW_option_value_item_in_option_value_object489)
                        option_value_item39 = self.option_value_item()

                        self._state.following.pop()
                        stream_option_value_item.add(option_value_item39.tree)


                    else:
                        break #loop6
                BLOCK_CLOSE40=self.match(self.input, BLOCK_CLOSE, self.FOLLOW_BLOCK_CLOSE_in_option_value_object492) 
                stream_BLOCK_CLOSE.add(BLOCK_CLOSE40)

                # AST Rewrite
                # elements: option_value_item
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 91:6: -> ^( OPTION_VALUE_OBJECT ( option_value_item )* )
                # proto_parser.g:91:9: ^( OPTION_VALUE_OBJECT ( option_value_item )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTION_VALUE_OBJECT, "OPTION_VALUE_OBJECT"), root_1)

                # proto_parser.g:91:31: ( option_value_item )*
                while stream_option_value_item.hasNext():
                    self._adaptor.addChild(root_1, stream_option_value_item.nextTree())


                stream_option_value_item.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "option_value_object"

    class option_value_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.option_value_item_return, self).__init__()

            self.tree = None




    # $ANTLR start "option_value_item"
    # proto_parser.g:94:1: option_value_item : IDENTIFIER COLON option_all_value -> ^( OPTION_VALUE_ITEM IDENTIFIER option_all_value ) ;
    def option_value_item(self, ):

        retval = self.option_value_item_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER41 = None
        COLON42 = None
        option_all_value43 = None


        IDENTIFIER41_tree = None
        COLON42_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_option_all_value = RewriteRuleSubtreeStream(self._adaptor, "rule option_all_value")
        try:
            try:
                # proto_parser.g:95:3: ( IDENTIFIER COLON option_all_value -> ^( OPTION_VALUE_ITEM IDENTIFIER option_all_value ) )
                # proto_parser.g:95:6: IDENTIFIER COLON option_all_value
                pass 
                IDENTIFIER41=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_option_value_item520) 
                stream_IDENTIFIER.add(IDENTIFIER41)
                COLON42=self.match(self.input, COLON, self.FOLLOW_COLON_in_option_value_item522) 
                stream_COLON.add(COLON42)
                self._state.following.append(self.FOLLOW_option_all_value_in_option_value_item524)
                option_all_value43 = self.option_all_value()

                self._state.following.pop()
                stream_option_all_value.add(option_all_value43.tree)

                # AST Rewrite
                # elements: option_all_value, IDENTIFIER
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 96:6: -> ^( OPTION_VALUE_ITEM IDENTIFIER option_all_value )
                # proto_parser.g:96:9: ^( OPTION_VALUE_ITEM IDENTIFIER option_all_value )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTION_VALUE_ITEM, "OPTION_VALUE_ITEM"), root_1)

                self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                self._adaptor.addChild(root_1, stream_option_all_value.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "option_value_item"

    class option_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.option_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "option_name"
    # proto_parser.g:99:1: option_name : ( IDENTIFIER -> ^( OPTION_PREDEFINED IDENTIFIER ) | PAREN_OPEN all_identifier PAREN_CLOSE ( FIELD_IDENTIFIER )* -> ^( OPTION_CUSTOMIZED all_identifier ( FIELD_IDENTIFIER )* ) );
    def option_name(self, ):

        retval = self.option_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER44 = None
        PAREN_OPEN45 = None
        PAREN_CLOSE47 = None
        FIELD_IDENTIFIER48 = None
        all_identifier46 = None


        IDENTIFIER44_tree = None
        PAREN_OPEN45_tree = None
        PAREN_CLOSE47_tree = None
        FIELD_IDENTIFIER48_tree = None
        stream_FIELD_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token FIELD_IDENTIFIER")
        stream_PAREN_OPEN = RewriteRuleTokenStream(self._adaptor, "token PAREN_OPEN")
        stream_PAREN_CLOSE = RewriteRuleTokenStream(self._adaptor, "token PAREN_CLOSE")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_all_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule all_identifier")
        try:
            try:
                # proto_parser.g:100:3: ( IDENTIFIER -> ^( OPTION_PREDEFINED IDENTIFIER ) | PAREN_OPEN all_identifier PAREN_CLOSE ( FIELD_IDENTIFIER )* -> ^( OPTION_CUSTOMIZED all_identifier ( FIELD_IDENTIFIER )* ) )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == IDENTIFIER) :
                    alt8 = 1
                elif (LA8_0 == PAREN_OPEN) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # proto_parser.g:100:6: IDENTIFIER
                    pass 
                    IDENTIFIER44=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_option_name553) 
                    stream_IDENTIFIER.add(IDENTIFIER44)

                    # AST Rewrite
                    # elements: IDENTIFIER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 101:6: -> ^( OPTION_PREDEFINED IDENTIFIER )
                    # proto_parser.g:101:9: ^( OPTION_PREDEFINED IDENTIFIER )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTION_PREDEFINED, "OPTION_PREDEFINED"), root_1)

                    self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                elif alt8 == 2:
                    # proto_parser.g:102:6: PAREN_OPEN all_identifier PAREN_CLOSE ( FIELD_IDENTIFIER )*
                    pass 
                    PAREN_OPEN45=self.match(self.input, PAREN_OPEN, self.FOLLOW_PAREN_OPEN_in_option_name573) 
                    stream_PAREN_OPEN.add(PAREN_OPEN45)
                    self._state.following.append(self.FOLLOW_all_identifier_in_option_name575)
                    all_identifier46 = self.all_identifier()

                    self._state.following.pop()
                    stream_all_identifier.add(all_identifier46.tree)
                    PAREN_CLOSE47=self.match(self.input, PAREN_CLOSE, self.FOLLOW_PAREN_CLOSE_in_option_name577) 
                    stream_PAREN_CLOSE.add(PAREN_CLOSE47)
                    # proto_parser.g:102:44: ( FIELD_IDENTIFIER )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == FIELD_IDENTIFIER) :
                            alt7 = 1


                        if alt7 == 1:
                            # proto_parser.g:102:44: FIELD_IDENTIFIER
                            pass 
                            FIELD_IDENTIFIER48=self.match(self.input, FIELD_IDENTIFIER, self.FOLLOW_FIELD_IDENTIFIER_in_option_name579) 
                            stream_FIELD_IDENTIFIER.add(FIELD_IDENTIFIER48)


                        else:
                            break #loop7

                    # AST Rewrite
                    # elements: FIELD_IDENTIFIER, all_identifier
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 103:6: -> ^( OPTION_CUSTOMIZED all_identifier ( FIELD_IDENTIFIER )* )
                    # proto_parser.g:103:9: ^( OPTION_CUSTOMIZED all_identifier ( FIELD_IDENTIFIER )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OPTION_CUSTOMIZED, "OPTION_CUSTOMIZED"), root_1)

                    self._adaptor.addChild(root_1, stream_all_identifier.nextTree())
                    # proto_parser.g:103:44: ( FIELD_IDENTIFIER )*
                    while stream_FIELD_IDENTIFIER.hasNext():
                        self._adaptor.addChild(root_1, stream_FIELD_IDENTIFIER.nextNode())


                    stream_FIELD_IDENTIFIER.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "option_name"

    class enum_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.enum_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "enum_def"
    # proto_parser.g:108:1: enum_def : ENUM_LITERAL enum_name BLOCK_OPEN enum_content BLOCK_CLOSE -> ^( ENUM_LITERAL enum_name enum_content ) ;
    def enum_def(self, ):

        retval = self.enum_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ENUM_LITERAL49 = None
        BLOCK_OPEN51 = None
        BLOCK_CLOSE53 = None
        enum_name50 = None

        enum_content52 = None


        ENUM_LITERAL49_tree = None
        BLOCK_OPEN51_tree = None
        BLOCK_CLOSE53_tree = None
        stream_BLOCK_OPEN = RewriteRuleTokenStream(self._adaptor, "token BLOCK_OPEN")
        stream_ENUM_LITERAL = RewriteRuleTokenStream(self._adaptor, "token ENUM_LITERAL")
        stream_BLOCK_CLOSE = RewriteRuleTokenStream(self._adaptor, "token BLOCK_CLOSE")
        stream_enum_name = RewriteRuleSubtreeStream(self._adaptor, "rule enum_name")
        stream_enum_content = RewriteRuleSubtreeStream(self._adaptor, "rule enum_content")
        try:
            try:
                # proto_parser.g:109:3: ( ENUM_LITERAL enum_name BLOCK_OPEN enum_content BLOCK_CLOSE -> ^( ENUM_LITERAL enum_name enum_content ) )
                # proto_parser.g:109:6: ENUM_LITERAL enum_name BLOCK_OPEN enum_content BLOCK_CLOSE
                pass 
                ENUM_LITERAL49=self.match(self.input, ENUM_LITERAL, self.FOLLOW_ENUM_LITERAL_in_enum_def612) 
                stream_ENUM_LITERAL.add(ENUM_LITERAL49)
                self._state.following.append(self.FOLLOW_enum_name_in_enum_def614)
                enum_name50 = self.enum_name()

                self._state.following.pop()
                stream_enum_name.add(enum_name50.tree)
                BLOCK_OPEN51=self.match(self.input, BLOCK_OPEN, self.FOLLOW_BLOCK_OPEN_in_enum_def616) 
                stream_BLOCK_OPEN.add(BLOCK_OPEN51)
                self._state.following.append(self.FOLLOW_enum_content_in_enum_def618)
                enum_content52 = self.enum_content()

                self._state.following.pop()
                stream_enum_content.add(enum_content52.tree)
                BLOCK_CLOSE53=self.match(self.input, BLOCK_CLOSE, self.FOLLOW_BLOCK_CLOSE_in_enum_def620) 
                stream_BLOCK_CLOSE.add(BLOCK_CLOSE53)

                # AST Rewrite
                # elements: enum_name, enum_content, ENUM_LITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 110:6: -> ^( ENUM_LITERAL enum_name enum_content )
                # proto_parser.g:110:9: ^( ENUM_LITERAL enum_name enum_content )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_ENUM_LITERAL.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_enum_name.nextTree())
                self._adaptor.addChild(root_1, stream_enum_content.nextTree())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "enum_def"

    class enum_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.enum_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "enum_name"
    # proto_parser.g:113:1: enum_name : IDENTIFIER ;
    def enum_name(self, ):

        retval = self.enum_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER54 = None

        IDENTIFIER54_tree = None

        try:
            try:
                # proto_parser.g:113:11: ( IDENTIFIER )
                # proto_parser.g:113:13: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER54=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_enum_name646)

                IDENTIFIER54_tree = self._adaptor.createWithPayload(IDENTIFIER54)
                self._adaptor.addChild(root_0, IDENTIFIER54_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "enum_name"

    class enum_content_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.enum_content_return, self).__init__()

            self.tree = None




    # $ANTLR start "enum_content"
    # proto_parser.g:115:1: enum_content : ( option_line_def | enum_item_def )* ;
    def enum_content(self, ):

        retval = self.enum_content_return()
        retval.start = self.input.LT(1)

        root_0 = None

        option_line_def55 = None

        enum_item_def56 = None



        try:
            try:
                # proto_parser.g:115:14: ( ( option_line_def | enum_item_def )* )
                # proto_parser.g:115:16: ( option_line_def | enum_item_def )*
                pass 
                root_0 = self._adaptor.nil()

                # proto_parser.g:115:16: ( option_line_def | enum_item_def )*
                while True: #loop9
                    alt9 = 3
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == OPTION_LITERAL) :
                        alt9 = 1
                    elif (LA9_0 == IDENTIFIER) :
                        alt9 = 2


                    if alt9 == 1:
                        # proto_parser.g:115:17: option_line_def
                        pass 
                        self._state.following.append(self.FOLLOW_option_line_def_in_enum_content656)
                        option_line_def55 = self.option_line_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, option_line_def55.tree)


                    elif alt9 == 2:
                        # proto_parser.g:115:35: enum_item_def
                        pass 
                        self._state.following.append(self.FOLLOW_enum_item_def_in_enum_content660)
                        enum_item_def56 = self.enum_item_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, enum_item_def56.tree)


                    else:
                        break #loop9



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "enum_content"

    class enum_item_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.enum_item_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "enum_item_def"
    # proto_parser.g:117:1: enum_item_def : IDENTIFIER EQUALS INTEGER_LITERAL ( option_field_def )? ITEM_TERMINATOR -> ^( ENUM_FIELD IDENTIFIER INTEGER_LITERAL ( option_field_def )? ) ;
    def enum_item_def(self, ):

        retval = self.enum_item_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER57 = None
        EQUALS58 = None
        INTEGER_LITERAL59 = None
        ITEM_TERMINATOR61 = None
        option_field_def60 = None


        IDENTIFIER57_tree = None
        EQUALS58_tree = None
        INTEGER_LITERAL59_tree = None
        ITEM_TERMINATOR61_tree = None
        stream_EQUALS = RewriteRuleTokenStream(self._adaptor, "token EQUALS")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_INTEGER_LITERAL = RewriteRuleTokenStream(self._adaptor, "token INTEGER_LITERAL")
        stream_ITEM_TERMINATOR = RewriteRuleTokenStream(self._adaptor, "token ITEM_TERMINATOR")
        stream_option_field_def = RewriteRuleSubtreeStream(self._adaptor, "rule option_field_def")
        try:
            try:
                # proto_parser.g:118:3: ( IDENTIFIER EQUALS INTEGER_LITERAL ( option_field_def )? ITEM_TERMINATOR -> ^( ENUM_FIELD IDENTIFIER INTEGER_LITERAL ( option_field_def )? ) )
                # proto_parser.g:118:6: IDENTIFIER EQUALS INTEGER_LITERAL ( option_field_def )? ITEM_TERMINATOR
                pass 
                IDENTIFIER57=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_enum_item_def674) 
                stream_IDENTIFIER.add(IDENTIFIER57)
                EQUALS58=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_enum_item_def676) 
                stream_EQUALS.add(EQUALS58)
                INTEGER_LITERAL59=self.match(self.input, INTEGER_LITERAL, self.FOLLOW_INTEGER_LITERAL_in_enum_item_def678) 
                stream_INTEGER_LITERAL.add(INTEGER_LITERAL59)
                # proto_parser.g:118:40: ( option_field_def )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == BRACKET_OPEN) :
                    alt10 = 1
                if alt10 == 1:
                    # proto_parser.g:118:40: option_field_def
                    pass 
                    self._state.following.append(self.FOLLOW_option_field_def_in_enum_item_def680)
                    option_field_def60 = self.option_field_def()

                    self._state.following.pop()
                    stream_option_field_def.add(option_field_def60.tree)



                ITEM_TERMINATOR61=self.match(self.input, ITEM_TERMINATOR, self.FOLLOW_ITEM_TERMINATOR_in_enum_item_def683) 
                stream_ITEM_TERMINATOR.add(ITEM_TERMINATOR61)

                # AST Rewrite
                # elements: INTEGER_LITERAL, IDENTIFIER, option_field_def
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 119:6: -> ^( ENUM_FIELD IDENTIFIER INTEGER_LITERAL ( option_field_def )? )
                # proto_parser.g:119:9: ^( ENUM_FIELD IDENTIFIER INTEGER_LITERAL ( option_field_def )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ENUM_FIELD, "ENUM_FIELD"), root_1)

                self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                self._adaptor.addChild(root_1, stream_INTEGER_LITERAL.nextNode())
                # proto_parser.g:119:49: ( option_field_def )?
                if stream_option_field_def.hasNext():
                    self._adaptor.addChild(root_1, stream_option_field_def.nextTree())


                stream_option_field_def.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "enum_item_def"

    class message_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.message_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "message_def"
    # proto_parser.g:124:1: message_def : MESSAGE_LITERAL message_name BLOCK_OPEN ( message_content )? BLOCK_CLOSE -> ^( MESSAGE_LITERAL message_name ( message_content )? ) ;
    def message_def(self, ):

        retval = self.message_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MESSAGE_LITERAL62 = None
        BLOCK_OPEN64 = None
        BLOCK_CLOSE66 = None
        message_name63 = None

        message_content65 = None


        MESSAGE_LITERAL62_tree = None
        BLOCK_OPEN64_tree = None
        BLOCK_CLOSE66_tree = None
        stream_BLOCK_OPEN = RewriteRuleTokenStream(self._adaptor, "token BLOCK_OPEN")
        stream_MESSAGE_LITERAL = RewriteRuleTokenStream(self._adaptor, "token MESSAGE_LITERAL")
        stream_BLOCK_CLOSE = RewriteRuleTokenStream(self._adaptor, "token BLOCK_CLOSE")
        stream_message_name = RewriteRuleSubtreeStream(self._adaptor, "rule message_name")
        stream_message_content = RewriteRuleSubtreeStream(self._adaptor, "rule message_content")
        try:
            try:
                # proto_parser.g:125:3: ( MESSAGE_LITERAL message_name BLOCK_OPEN ( message_content )? BLOCK_CLOSE -> ^( MESSAGE_LITERAL message_name ( message_content )? ) )
                # proto_parser.g:125:6: MESSAGE_LITERAL message_name BLOCK_OPEN ( message_content )? BLOCK_CLOSE
                pass 
                MESSAGE_LITERAL62=self.match(self.input, MESSAGE_LITERAL, self.FOLLOW_MESSAGE_LITERAL_in_message_def717) 
                stream_MESSAGE_LITERAL.add(MESSAGE_LITERAL62)
                self._state.following.append(self.FOLLOW_message_name_in_message_def719)
                message_name63 = self.message_name()

                self._state.following.pop()
                stream_message_name.add(message_name63.tree)
                BLOCK_OPEN64=self.match(self.input, BLOCK_OPEN, self.FOLLOW_BLOCK_OPEN_in_message_def721) 
                stream_BLOCK_OPEN.add(BLOCK_OPEN64)
                # proto_parser.g:125:46: ( message_content )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((OPTION_LITERAL <= LA11_0 <= MESSAGE_LITERAL) or LA11_0 == EXTENSIONS_DEF_LITERAL or LA11_0 == PROTOBUF_SCOPE_LITERAL) :
                    alt11 = 1
                if alt11 == 1:
                    # proto_parser.g:125:46: message_content
                    pass 
                    self._state.following.append(self.FOLLOW_message_content_in_message_def723)
                    message_content65 = self.message_content()

                    self._state.following.pop()
                    stream_message_content.add(message_content65.tree)



                BLOCK_CLOSE66=self.match(self.input, BLOCK_CLOSE, self.FOLLOW_BLOCK_CLOSE_in_message_def726) 
                stream_BLOCK_CLOSE.add(BLOCK_CLOSE66)

                # AST Rewrite
                # elements: MESSAGE_LITERAL, message_name, message_content
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 126:6: -> ^( MESSAGE_LITERAL message_name ( message_content )? )
                # proto_parser.g:126:9: ^( MESSAGE_LITERAL message_name ( message_content )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_MESSAGE_LITERAL.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_message_name.nextTree())
                # proto_parser.g:126:40: ( message_content )?
                if stream_message_content.hasNext():
                    self._adaptor.addChild(root_1, stream_message_content.nextTree())


                stream_message_content.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "message_def"

    class message_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.message_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "message_name"
    # proto_parser.g:129:1: message_name : IDENTIFIER ;
    def message_name(self, ):

        retval = self.message_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER67 = None

        IDENTIFIER67_tree = None

        try:
            try:
                # proto_parser.g:129:14: ( IDENTIFIER )
                # proto_parser.g:129:16: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER67=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_message_name753)

                IDENTIFIER67_tree = self._adaptor.createWithPayload(IDENTIFIER67)
                self._adaptor.addChild(root_0, IDENTIFIER67_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "message_name"

    class message_content_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.message_content_return, self).__init__()

            self.tree = None




    # $ANTLR start "message_content"
    # proto_parser.g:131:1: message_content : ( option_line_def | message_item_def | message_def | enum_def | message_ext_def )+ ;
    def message_content(self, ):

        retval = self.message_content_return()
        retval.start = self.input.LT(1)

        root_0 = None

        option_line_def68 = None

        message_item_def69 = None

        message_def70 = None

        enum_def71 = None

        message_ext_def72 = None



        try:
            try:
                # proto_parser.g:131:17: ( ( option_line_def | message_item_def | message_def | enum_def | message_ext_def )+ )
                # proto_parser.g:131:19: ( option_line_def | message_item_def | message_def | enum_def | message_ext_def )+
                pass 
                root_0 = self._adaptor.nil()

                # proto_parser.g:131:19: ( option_line_def | message_item_def | message_def | enum_def | message_ext_def )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 6
                    LA12 = self.input.LA(1)
                    if LA12 == OPTION_LITERAL:
                        alt12 = 1
                    elif LA12 == PROTOBUF_SCOPE_LITERAL:
                        alt12 = 2
                    elif LA12 == MESSAGE_LITERAL:
                        alt12 = 3
                    elif LA12 == ENUM_LITERAL:
                        alt12 = 4
                    elif LA12 == EXTENSIONS_DEF_LITERAL:
                        alt12 = 5

                    if alt12 == 1:
                        # proto_parser.g:131:20: option_line_def
                        pass 
                        self._state.following.append(self.FOLLOW_option_line_def_in_message_content763)
                        option_line_def68 = self.option_line_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, option_line_def68.tree)


                    elif alt12 == 2:
                        # proto_parser.g:131:38: message_item_def
                        pass 
                        self._state.following.append(self.FOLLOW_message_item_def_in_message_content767)
                        message_item_def69 = self.message_item_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, message_item_def69.tree)


                    elif alt12 == 3:
                        # proto_parser.g:131:57: message_def
                        pass 
                        self._state.following.append(self.FOLLOW_message_def_in_message_content771)
                        message_def70 = self.message_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, message_def70.tree)


                    elif alt12 == 4:
                        # proto_parser.g:131:71: enum_def
                        pass 
                        self._state.following.append(self.FOLLOW_enum_def_in_message_content775)
                        enum_def71 = self.enum_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, enum_def71.tree)


                    elif alt12 == 5:
                        # proto_parser.g:131:82: message_ext_def
                        pass 
                        self._state.following.append(self.FOLLOW_message_ext_def_in_message_content779)
                        message_ext_def72 = self.message_ext_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, message_ext_def72.tree)


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "message_content"

    class message_item_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.message_item_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "message_item_def"
    # proto_parser.g:133:1: message_item_def : PROTOBUF_SCOPE_LITERAL proto_type IDENTIFIER EQUALS INTEGER_LITERAL ( option_field_def )? ITEM_TERMINATOR -> ^( MESSAGE_FIELD PROTOBUF_SCOPE_LITERAL proto_type IDENTIFIER INTEGER_LITERAL ( option_field_def )? ) ;
    def message_item_def(self, ):

        retval = self.message_item_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PROTOBUF_SCOPE_LITERAL73 = None
        IDENTIFIER75 = None
        EQUALS76 = None
        INTEGER_LITERAL77 = None
        ITEM_TERMINATOR79 = None
        proto_type74 = None

        option_field_def78 = None


        PROTOBUF_SCOPE_LITERAL73_tree = None
        IDENTIFIER75_tree = None
        EQUALS76_tree = None
        INTEGER_LITERAL77_tree = None
        ITEM_TERMINATOR79_tree = None
        stream_EQUALS = RewriteRuleTokenStream(self._adaptor, "token EQUALS")
        stream_PROTOBUF_SCOPE_LITERAL = RewriteRuleTokenStream(self._adaptor, "token PROTOBUF_SCOPE_LITERAL")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_INTEGER_LITERAL = RewriteRuleTokenStream(self._adaptor, "token INTEGER_LITERAL")
        stream_ITEM_TERMINATOR = RewriteRuleTokenStream(self._adaptor, "token ITEM_TERMINATOR")
        stream_proto_type = RewriteRuleSubtreeStream(self._adaptor, "rule proto_type")
        stream_option_field_def = RewriteRuleSubtreeStream(self._adaptor, "rule option_field_def")
        try:
            try:
                # proto_parser.g:134:3: ( PROTOBUF_SCOPE_LITERAL proto_type IDENTIFIER EQUALS INTEGER_LITERAL ( option_field_def )? ITEM_TERMINATOR -> ^( MESSAGE_FIELD PROTOBUF_SCOPE_LITERAL proto_type IDENTIFIER INTEGER_LITERAL ( option_field_def )? ) )
                # proto_parser.g:134:5: PROTOBUF_SCOPE_LITERAL proto_type IDENTIFIER EQUALS INTEGER_LITERAL ( option_field_def )? ITEM_TERMINATOR
                pass 
                PROTOBUF_SCOPE_LITERAL73=self.match(self.input, PROTOBUF_SCOPE_LITERAL, self.FOLLOW_PROTOBUF_SCOPE_LITERAL_in_message_item_def792) 
                stream_PROTOBUF_SCOPE_LITERAL.add(PROTOBUF_SCOPE_LITERAL73)
                self._state.following.append(self.FOLLOW_proto_type_in_message_item_def794)
                proto_type74 = self.proto_type()

                self._state.following.pop()
                stream_proto_type.add(proto_type74.tree)
                IDENTIFIER75=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_message_item_def796) 
                stream_IDENTIFIER.add(IDENTIFIER75)
                EQUALS76=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_message_item_def798) 
                stream_EQUALS.add(EQUALS76)
                INTEGER_LITERAL77=self.match(self.input, INTEGER_LITERAL, self.FOLLOW_INTEGER_LITERAL_in_message_item_def800) 
                stream_INTEGER_LITERAL.add(INTEGER_LITERAL77)
                # proto_parser.g:134:73: ( option_field_def )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == BRACKET_OPEN) :
                    alt13 = 1
                if alt13 == 1:
                    # proto_parser.g:134:73: option_field_def
                    pass 
                    self._state.following.append(self.FOLLOW_option_field_def_in_message_item_def802)
                    option_field_def78 = self.option_field_def()

                    self._state.following.pop()
                    stream_option_field_def.add(option_field_def78.tree)



                ITEM_TERMINATOR79=self.match(self.input, ITEM_TERMINATOR, self.FOLLOW_ITEM_TERMINATOR_in_message_item_def805) 
                stream_ITEM_TERMINATOR.add(ITEM_TERMINATOR79)

                # AST Rewrite
                # elements: INTEGER_LITERAL, option_field_def, proto_type, PROTOBUF_SCOPE_LITERAL, IDENTIFIER
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 135:6: -> ^( MESSAGE_FIELD PROTOBUF_SCOPE_LITERAL proto_type IDENTIFIER INTEGER_LITERAL ( option_field_def )? )
                # proto_parser.g:135:9: ^( MESSAGE_FIELD PROTOBUF_SCOPE_LITERAL proto_type IDENTIFIER INTEGER_LITERAL ( option_field_def )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MESSAGE_FIELD, "MESSAGE_FIELD"), root_1)

                self._adaptor.addChild(root_1, stream_PROTOBUF_SCOPE_LITERAL.nextNode())
                self._adaptor.addChild(root_1, stream_proto_type.nextTree())
                self._adaptor.addChild(root_1, stream_IDENTIFIER.nextNode())
                self._adaptor.addChild(root_1, stream_INTEGER_LITERAL.nextNode())
                # proto_parser.g:135:86: ( option_field_def )?
                if stream_option_field_def.hasNext():
                    self._adaptor.addChild(root_1, stream_option_field_def.nextTree())


                stream_option_field_def.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "message_item_def"

    class message_ext_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.message_ext_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "message_ext_def"
    # proto_parser.g:138:1: message_ext_def : EXTENSIONS_DEF_LITERAL INTEGER_LITERAL EXTENSIONS_TO_LITERAL (v= INTEGER_LITERAL | v= EXTENSIONS_MAX_LITERAL ) ITEM_TERMINATOR -> ^( EXTENSIONS_DEF_LITERAL INTEGER_LITERAL $v) ;
    def message_ext_def(self, ):

        retval = self.message_ext_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        v = None
        EXTENSIONS_DEF_LITERAL80 = None
        INTEGER_LITERAL81 = None
        EXTENSIONS_TO_LITERAL82 = None
        ITEM_TERMINATOR83 = None

        v_tree = None
        EXTENSIONS_DEF_LITERAL80_tree = None
        INTEGER_LITERAL81_tree = None
        EXTENSIONS_TO_LITERAL82_tree = None
        ITEM_TERMINATOR83_tree = None
        stream_EXTENSIONS_MAX_LITERAL = RewriteRuleTokenStream(self._adaptor, "token EXTENSIONS_MAX_LITERAL")
        stream_EXTENSIONS_TO_LITERAL = RewriteRuleTokenStream(self._adaptor, "token EXTENSIONS_TO_LITERAL")
        stream_EXTENSIONS_DEF_LITERAL = RewriteRuleTokenStream(self._adaptor, "token EXTENSIONS_DEF_LITERAL")
        stream_INTEGER_LITERAL = RewriteRuleTokenStream(self._adaptor, "token INTEGER_LITERAL")
        stream_ITEM_TERMINATOR = RewriteRuleTokenStream(self._adaptor, "token ITEM_TERMINATOR")

        try:
            try:
                # proto_parser.g:139:3: ( EXTENSIONS_DEF_LITERAL INTEGER_LITERAL EXTENSIONS_TO_LITERAL (v= INTEGER_LITERAL | v= EXTENSIONS_MAX_LITERAL ) ITEM_TERMINATOR -> ^( EXTENSIONS_DEF_LITERAL INTEGER_LITERAL $v) )
                # proto_parser.g:139:5: EXTENSIONS_DEF_LITERAL INTEGER_LITERAL EXTENSIONS_TO_LITERAL (v= INTEGER_LITERAL | v= EXTENSIONS_MAX_LITERAL ) ITEM_TERMINATOR
                pass 
                EXTENSIONS_DEF_LITERAL80=self.match(self.input, EXTENSIONS_DEF_LITERAL, self.FOLLOW_EXTENSIONS_DEF_LITERAL_in_message_ext_def840) 
                stream_EXTENSIONS_DEF_LITERAL.add(EXTENSIONS_DEF_LITERAL80)
                INTEGER_LITERAL81=self.match(self.input, INTEGER_LITERAL, self.FOLLOW_INTEGER_LITERAL_in_message_ext_def842) 
                stream_INTEGER_LITERAL.add(INTEGER_LITERAL81)
                EXTENSIONS_TO_LITERAL82=self.match(self.input, EXTENSIONS_TO_LITERAL, self.FOLLOW_EXTENSIONS_TO_LITERAL_in_message_ext_def844) 
                stream_EXTENSIONS_TO_LITERAL.add(EXTENSIONS_TO_LITERAL82)
                # proto_parser.g:139:66: (v= INTEGER_LITERAL | v= EXTENSIONS_MAX_LITERAL )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == INTEGER_LITERAL) :
                    alt14 = 1
                elif (LA14_0 == EXTENSIONS_MAX_LITERAL) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # proto_parser.g:139:67: v= INTEGER_LITERAL
                    pass 
                    v=self.match(self.input, INTEGER_LITERAL, self.FOLLOW_INTEGER_LITERAL_in_message_ext_def849) 
                    stream_INTEGER_LITERAL.add(v)


                elif alt14 == 2:
                    # proto_parser.g:139:87: v= EXTENSIONS_MAX_LITERAL
                    pass 
                    v=self.match(self.input, EXTENSIONS_MAX_LITERAL, self.FOLLOW_EXTENSIONS_MAX_LITERAL_in_message_ext_def855) 
                    stream_EXTENSIONS_MAX_LITERAL.add(v)



                ITEM_TERMINATOR83=self.match(self.input, ITEM_TERMINATOR, self.FOLLOW_ITEM_TERMINATOR_in_message_ext_def858) 
                stream_ITEM_TERMINATOR.add(ITEM_TERMINATOR83)

                # AST Rewrite
                # elements: INTEGER_LITERAL, EXTENSIONS_DEF_LITERAL, v
                # token labels: v
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_v = RewriteRuleTokenStream(self._adaptor, "token v", v)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 140:5: -> ^( EXTENSIONS_DEF_LITERAL INTEGER_LITERAL $v)
                # proto_parser.g:140:8: ^( EXTENSIONS_DEF_LITERAL INTEGER_LITERAL $v)
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_EXTENSIONS_DEF_LITERAL.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_INTEGER_LITERAL.nextNode())
                self._adaptor.addChild(root_1, stream_v.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "message_ext_def"

    class ext_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.ext_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "ext_def"
    # proto_parser.g:145:1: ext_def : EXTEND_LITERAL ext_name BLOCK_OPEN ( ext_content )? BLOCK_CLOSE -> ^( EXTEND_LITERAL ext_name ( ext_content )? ) ;
    def ext_def(self, ):

        retval = self.ext_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EXTEND_LITERAL84 = None
        BLOCK_OPEN86 = None
        BLOCK_CLOSE88 = None
        ext_name85 = None

        ext_content87 = None


        EXTEND_LITERAL84_tree = None
        BLOCK_OPEN86_tree = None
        BLOCK_CLOSE88_tree = None
        stream_BLOCK_OPEN = RewriteRuleTokenStream(self._adaptor, "token BLOCK_OPEN")
        stream_BLOCK_CLOSE = RewriteRuleTokenStream(self._adaptor, "token BLOCK_CLOSE")
        stream_EXTEND_LITERAL = RewriteRuleTokenStream(self._adaptor, "token EXTEND_LITERAL")
        stream_ext_name = RewriteRuleSubtreeStream(self._adaptor, "rule ext_name")
        stream_ext_content = RewriteRuleSubtreeStream(self._adaptor, "rule ext_content")
        try:
            try:
                # proto_parser.g:146:3: ( EXTEND_LITERAL ext_name BLOCK_OPEN ( ext_content )? BLOCK_CLOSE -> ^( EXTEND_LITERAL ext_name ( ext_content )? ) )
                # proto_parser.g:146:6: EXTEND_LITERAL ext_name BLOCK_OPEN ( ext_content )? BLOCK_CLOSE
                pass 
                EXTEND_LITERAL84=self.match(self.input, EXTEND_LITERAL, self.FOLLOW_EXTEND_LITERAL_in_ext_def889) 
                stream_EXTEND_LITERAL.add(EXTEND_LITERAL84)
                self._state.following.append(self.FOLLOW_ext_name_in_ext_def891)
                ext_name85 = self.ext_name()

                self._state.following.pop()
                stream_ext_name.add(ext_name85.tree)
                BLOCK_OPEN86=self.match(self.input, BLOCK_OPEN, self.FOLLOW_BLOCK_OPEN_in_ext_def893) 
                stream_BLOCK_OPEN.add(BLOCK_OPEN86)
                # proto_parser.g:146:41: ( ext_content )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if ((OPTION_LITERAL <= LA15_0 <= MESSAGE_LITERAL) or LA15_0 == PROTOBUF_SCOPE_LITERAL) :
                    alt15 = 1
                if alt15 == 1:
                    # proto_parser.g:146:41: ext_content
                    pass 
                    self._state.following.append(self.FOLLOW_ext_content_in_ext_def895)
                    ext_content87 = self.ext_content()

                    self._state.following.pop()
                    stream_ext_content.add(ext_content87.tree)



                BLOCK_CLOSE88=self.match(self.input, BLOCK_CLOSE, self.FOLLOW_BLOCK_CLOSE_in_ext_def898) 
                stream_BLOCK_CLOSE.add(BLOCK_CLOSE88)

                # AST Rewrite
                # elements: ext_content, ext_name, EXTEND_LITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 147:6: -> ^( EXTEND_LITERAL ext_name ( ext_content )? )
                # proto_parser.g:147:9: ^( EXTEND_LITERAL ext_name ( ext_content )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_EXTEND_LITERAL.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_ext_name.nextTree())
                # proto_parser.g:147:35: ( ext_content )?
                if stream_ext_content.hasNext():
                    self._adaptor.addChild(root_1, stream_ext_content.nextTree())


                stream_ext_content.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ext_def"

    class ext_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.ext_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "ext_name"
    # proto_parser.g:150:1: ext_name : all_identifier ;
    def ext_name(self, ):

        retval = self.ext_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        all_identifier89 = None



        try:
            try:
                # proto_parser.g:150:10: ( all_identifier )
                # proto_parser.g:150:12: all_identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_all_identifier_in_ext_name925)
                all_identifier89 = self.all_identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, all_identifier89.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ext_name"

    class ext_content_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.ext_content_return, self).__init__()

            self.tree = None




    # $ANTLR start "ext_content"
    # proto_parser.g:152:1: ext_content : ( option_line_def | message_item_def | message_def | enum_def )+ ;
    def ext_content(self, ):

        retval = self.ext_content_return()
        retval.start = self.input.LT(1)

        root_0 = None

        option_line_def90 = None

        message_item_def91 = None

        message_def92 = None

        enum_def93 = None



        try:
            try:
                # proto_parser.g:152:13: ( ( option_line_def | message_item_def | message_def | enum_def )+ )
                # proto_parser.g:152:15: ( option_line_def | message_item_def | message_def | enum_def )+
                pass 
                root_0 = self._adaptor.nil()

                # proto_parser.g:152:15: ( option_line_def | message_item_def | message_def | enum_def )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 5
                    LA16 = self.input.LA(1)
                    if LA16 == OPTION_LITERAL:
                        alt16 = 1
                    elif LA16 == PROTOBUF_SCOPE_LITERAL:
                        alt16 = 2
                    elif LA16 == MESSAGE_LITERAL:
                        alt16 = 3
                    elif LA16 == ENUM_LITERAL:
                        alt16 = 4

                    if alt16 == 1:
                        # proto_parser.g:152:16: option_line_def
                        pass 
                        self._state.following.append(self.FOLLOW_option_line_def_in_ext_content935)
                        option_line_def90 = self.option_line_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, option_line_def90.tree)


                    elif alt16 == 2:
                        # proto_parser.g:152:34: message_item_def
                        pass 
                        self._state.following.append(self.FOLLOW_message_item_def_in_ext_content939)
                        message_item_def91 = self.message_item_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, message_item_def91.tree)


                    elif alt16 == 3:
                        # proto_parser.g:152:53: message_def
                        pass 
                        self._state.following.append(self.FOLLOW_message_def_in_ext_content943)
                        message_def92 = self.message_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, message_def92.tree)


                    elif alt16 == 4:
                        # proto_parser.g:152:67: enum_def
                        pass 
                        self._state.following.append(self.FOLLOW_enum_def_in_ext_content947)
                        enum_def93 = self.enum_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, enum_def93.tree)


                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ext_content"

    class service_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.service_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "service_def"
    # proto_parser.g:156:1: service_def : SERVICE_LITERAL service_name BLOCK_OPEN ( service_content )? BLOCK_CLOSE -> ^( SERVICE_LITERAL service_name ( service_content )? ) ;
    def service_def(self, ):

        retval = self.service_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SERVICE_LITERAL94 = None
        BLOCK_OPEN96 = None
        BLOCK_CLOSE98 = None
        service_name95 = None

        service_content97 = None


        SERVICE_LITERAL94_tree = None
        BLOCK_OPEN96_tree = None
        BLOCK_CLOSE98_tree = None
        stream_BLOCK_OPEN = RewriteRuleTokenStream(self._adaptor, "token BLOCK_OPEN")
        stream_SERVICE_LITERAL = RewriteRuleTokenStream(self._adaptor, "token SERVICE_LITERAL")
        stream_BLOCK_CLOSE = RewriteRuleTokenStream(self._adaptor, "token BLOCK_CLOSE")
        stream_service_content = RewriteRuleSubtreeStream(self._adaptor, "rule service_content")
        stream_service_name = RewriteRuleSubtreeStream(self._adaptor, "rule service_name")
        try:
            try:
                # proto_parser.g:157:3: ( SERVICE_LITERAL service_name BLOCK_OPEN ( service_content )? BLOCK_CLOSE -> ^( SERVICE_LITERAL service_name ( service_content )? ) )
                # proto_parser.g:157:6: SERVICE_LITERAL service_name BLOCK_OPEN ( service_content )? BLOCK_CLOSE
                pass 
                SERVICE_LITERAL94=self.match(self.input, SERVICE_LITERAL, self.FOLLOW_SERVICE_LITERAL_in_service_def963) 
                stream_SERVICE_LITERAL.add(SERVICE_LITERAL94)
                self._state.following.append(self.FOLLOW_service_name_in_service_def965)
                service_name95 = self.service_name()

                self._state.following.pop()
                stream_service_name.add(service_name95.tree)
                BLOCK_OPEN96=self.match(self.input, BLOCK_OPEN, self.FOLLOW_BLOCK_OPEN_in_service_def967) 
                stream_BLOCK_OPEN.add(BLOCK_OPEN96)
                # proto_parser.g:157:46: ( service_content )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == OPTION_LITERAL or LA17_0 == RPC_LITERAL) :
                    alt17 = 1
                if alt17 == 1:
                    # proto_parser.g:157:46: service_content
                    pass 
                    self._state.following.append(self.FOLLOW_service_content_in_service_def969)
                    service_content97 = self.service_content()

                    self._state.following.pop()
                    stream_service_content.add(service_content97.tree)



                BLOCK_CLOSE98=self.match(self.input, BLOCK_CLOSE, self.FOLLOW_BLOCK_CLOSE_in_service_def972) 
                stream_BLOCK_CLOSE.add(BLOCK_CLOSE98)

                # AST Rewrite
                # elements: service_content, SERVICE_LITERAL, service_name
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 158:6: -> ^( SERVICE_LITERAL service_name ( service_content )? )
                # proto_parser.g:158:9: ^( SERVICE_LITERAL service_name ( service_content )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_SERVICE_LITERAL.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_service_name.nextTree())
                # proto_parser.g:158:40: ( service_content )?
                if stream_service_content.hasNext():
                    self._adaptor.addChild(root_1, stream_service_content.nextTree())


                stream_service_content.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "service_def"

    class service_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.service_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "service_name"
    # proto_parser.g:161:1: service_name : IDENTIFIER ;
    def service_name(self, ):

        retval = self.service_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER99 = None

        IDENTIFIER99_tree = None

        try:
            try:
                # proto_parser.g:161:14: ( IDENTIFIER )
                # proto_parser.g:161:16: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER99=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_service_name999)

                IDENTIFIER99_tree = self._adaptor.createWithPayload(IDENTIFIER99)
                self._adaptor.addChild(root_0, IDENTIFIER99_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "service_name"

    class service_content_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.service_content_return, self).__init__()

            self.tree = None




    # $ANTLR start "service_content"
    # proto_parser.g:163:1: service_content : ( option_line_def | rpc_def )+ ;
    def service_content(self, ):

        retval = self.service_content_return()
        retval.start = self.input.LT(1)

        root_0 = None

        option_line_def100 = None

        rpc_def101 = None



        try:
            try:
                # proto_parser.g:163:17: ( ( option_line_def | rpc_def )+ )
                # proto_parser.g:163:19: ( option_line_def | rpc_def )+
                pass 
                root_0 = self._adaptor.nil()

                # proto_parser.g:163:19: ( option_line_def | rpc_def )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 3
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == OPTION_LITERAL) :
                        alt18 = 1
                    elif (LA18_0 == RPC_LITERAL) :
                        alt18 = 2


                    if alt18 == 1:
                        # proto_parser.g:163:20: option_line_def
                        pass 
                        self._state.following.append(self.FOLLOW_option_line_def_in_service_content1009)
                        option_line_def100 = self.option_line_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, option_line_def100.tree)


                    elif alt18 == 2:
                        # proto_parser.g:163:38: rpc_def
                        pass 
                        self._state.following.append(self.FOLLOW_rpc_def_in_service_content1013)
                        rpc_def101 = self.rpc_def()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, rpc_def101.tree)


                    else:
                        if cnt18 >= 1:
                            break #loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "service_content"

    class rpc_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.rpc_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "rpc_def"
    # proto_parser.g:165:1: rpc_def : RPC_LITERAL rpc_name PAREN_OPEN req_name PAREN_CLOSE RETURNS_LITERAL PAREN_OPEN resp_name PAREN_CLOSE ( BLOCK_OPEN ( option_line_def )* BLOCK_CLOSE ( ITEM_TERMINATOR )? | ITEM_TERMINATOR ) -> ^( RPC_LITERAL rpc_name req_name resp_name ( option_line_def )* ) ;
    def rpc_def(self, ):

        retval = self.rpc_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPC_LITERAL102 = None
        PAREN_OPEN104 = None
        PAREN_CLOSE106 = None
        RETURNS_LITERAL107 = None
        PAREN_OPEN108 = None
        PAREN_CLOSE110 = None
        BLOCK_OPEN111 = None
        BLOCK_CLOSE113 = None
        ITEM_TERMINATOR114 = None
        ITEM_TERMINATOR115 = None
        rpc_name103 = None

        req_name105 = None

        resp_name109 = None

        option_line_def112 = None


        RPC_LITERAL102_tree = None
        PAREN_OPEN104_tree = None
        PAREN_CLOSE106_tree = None
        RETURNS_LITERAL107_tree = None
        PAREN_OPEN108_tree = None
        PAREN_CLOSE110_tree = None
        BLOCK_OPEN111_tree = None
        BLOCK_CLOSE113_tree = None
        ITEM_TERMINATOR114_tree = None
        ITEM_TERMINATOR115_tree = None
        stream_BLOCK_OPEN = RewriteRuleTokenStream(self._adaptor, "token BLOCK_OPEN")
        stream_BLOCK_CLOSE = RewriteRuleTokenStream(self._adaptor, "token BLOCK_CLOSE")
        stream_PAREN_OPEN = RewriteRuleTokenStream(self._adaptor, "token PAREN_OPEN")
        stream_PAREN_CLOSE = RewriteRuleTokenStream(self._adaptor, "token PAREN_CLOSE")
        stream_ITEM_TERMINATOR = RewriteRuleTokenStream(self._adaptor, "token ITEM_TERMINATOR")
        stream_RPC_LITERAL = RewriteRuleTokenStream(self._adaptor, "token RPC_LITERAL")
        stream_RETURNS_LITERAL = RewriteRuleTokenStream(self._adaptor, "token RETURNS_LITERAL")
        stream_rpc_name = RewriteRuleSubtreeStream(self._adaptor, "rule rpc_name")
        stream_resp_name = RewriteRuleSubtreeStream(self._adaptor, "rule resp_name")
        stream_req_name = RewriteRuleSubtreeStream(self._adaptor, "rule req_name")
        stream_option_line_def = RewriteRuleSubtreeStream(self._adaptor, "rule option_line_def")
        try:
            try:
                # proto_parser.g:166:3: ( RPC_LITERAL rpc_name PAREN_OPEN req_name PAREN_CLOSE RETURNS_LITERAL PAREN_OPEN resp_name PAREN_CLOSE ( BLOCK_OPEN ( option_line_def )* BLOCK_CLOSE ( ITEM_TERMINATOR )? | ITEM_TERMINATOR ) -> ^( RPC_LITERAL rpc_name req_name resp_name ( option_line_def )* ) )
                # proto_parser.g:166:6: RPC_LITERAL rpc_name PAREN_OPEN req_name PAREN_CLOSE RETURNS_LITERAL PAREN_OPEN resp_name PAREN_CLOSE ( BLOCK_OPEN ( option_line_def )* BLOCK_CLOSE ( ITEM_TERMINATOR )? | ITEM_TERMINATOR )
                pass 
                RPC_LITERAL102=self.match(self.input, RPC_LITERAL, self.FOLLOW_RPC_LITERAL_in_rpc_def1028) 
                stream_RPC_LITERAL.add(RPC_LITERAL102)
                self._state.following.append(self.FOLLOW_rpc_name_in_rpc_def1030)
                rpc_name103 = self.rpc_name()

                self._state.following.pop()
                stream_rpc_name.add(rpc_name103.tree)
                PAREN_OPEN104=self.match(self.input, PAREN_OPEN, self.FOLLOW_PAREN_OPEN_in_rpc_def1032) 
                stream_PAREN_OPEN.add(PAREN_OPEN104)
                self._state.following.append(self.FOLLOW_req_name_in_rpc_def1034)
                req_name105 = self.req_name()

                self._state.following.pop()
                stream_req_name.add(req_name105.tree)
                PAREN_CLOSE106=self.match(self.input, PAREN_CLOSE, self.FOLLOW_PAREN_CLOSE_in_rpc_def1036) 
                stream_PAREN_CLOSE.add(PAREN_CLOSE106)
                RETURNS_LITERAL107=self.match(self.input, RETURNS_LITERAL, self.FOLLOW_RETURNS_LITERAL_in_rpc_def1038) 
                stream_RETURNS_LITERAL.add(RETURNS_LITERAL107)
                PAREN_OPEN108=self.match(self.input, PAREN_OPEN, self.FOLLOW_PAREN_OPEN_in_rpc_def1040) 
                stream_PAREN_OPEN.add(PAREN_OPEN108)
                self._state.following.append(self.FOLLOW_resp_name_in_rpc_def1042)
                resp_name109 = self.resp_name()

                self._state.following.pop()
                stream_resp_name.add(resp_name109.tree)
                PAREN_CLOSE110=self.match(self.input, PAREN_CLOSE, self.FOLLOW_PAREN_CLOSE_in_rpc_def1044) 
                stream_PAREN_CLOSE.add(PAREN_CLOSE110)
                # proto_parser.g:166:108: ( BLOCK_OPEN ( option_line_def )* BLOCK_CLOSE ( ITEM_TERMINATOR )? | ITEM_TERMINATOR )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == BLOCK_OPEN) :
                    alt21 = 1
                elif (LA21_0 == ITEM_TERMINATOR) :
                    alt21 = 2
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # proto_parser.g:166:109: BLOCK_OPEN ( option_line_def )* BLOCK_CLOSE ( ITEM_TERMINATOR )?
                    pass 
                    BLOCK_OPEN111=self.match(self.input, BLOCK_OPEN, self.FOLLOW_BLOCK_OPEN_in_rpc_def1047) 
                    stream_BLOCK_OPEN.add(BLOCK_OPEN111)
                    # proto_parser.g:166:120: ( option_line_def )*
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == OPTION_LITERAL) :
                            alt19 = 1


                        if alt19 == 1:
                            # proto_parser.g:166:120: option_line_def
                            pass 
                            self._state.following.append(self.FOLLOW_option_line_def_in_rpc_def1049)
                            option_line_def112 = self.option_line_def()

                            self._state.following.pop()
                            stream_option_line_def.add(option_line_def112.tree)


                        else:
                            break #loop19
                    BLOCK_CLOSE113=self.match(self.input, BLOCK_CLOSE, self.FOLLOW_BLOCK_CLOSE_in_rpc_def1052) 
                    stream_BLOCK_CLOSE.add(BLOCK_CLOSE113)
                    # proto_parser.g:166:149: ( ITEM_TERMINATOR )?
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == ITEM_TERMINATOR) :
                        alt20 = 1
                    if alt20 == 1:
                        # proto_parser.g:166:149: ITEM_TERMINATOR
                        pass 
                        ITEM_TERMINATOR114=self.match(self.input, ITEM_TERMINATOR, self.FOLLOW_ITEM_TERMINATOR_in_rpc_def1054) 
                        stream_ITEM_TERMINATOR.add(ITEM_TERMINATOR114)





                elif alt21 == 2:
                    # proto_parser.g:166:168: ITEM_TERMINATOR
                    pass 
                    ITEM_TERMINATOR115=self.match(self.input, ITEM_TERMINATOR, self.FOLLOW_ITEM_TERMINATOR_in_rpc_def1059) 
                    stream_ITEM_TERMINATOR.add(ITEM_TERMINATOR115)




                # AST Rewrite
                # elements: option_line_def, rpc_name, resp_name, req_name, RPC_LITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 167:6: -> ^( RPC_LITERAL rpc_name req_name resp_name ( option_line_def )* )
                # proto_parser.g:167:9: ^( RPC_LITERAL rpc_name req_name resp_name ( option_line_def )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(stream_RPC_LITERAL.nextNode(), root_1)

                self._adaptor.addChild(root_1, stream_rpc_name.nextTree())
                self._adaptor.addChild(root_1, stream_req_name.nextTree())
                self._adaptor.addChild(root_1, stream_resp_name.nextTree())
                # proto_parser.g:167:51: ( option_line_def )*
                while stream_option_line_def.hasNext():
                    self._adaptor.addChild(root_1, stream_option_line_def.nextTree())


                stream_option_line_def.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "rpc_def"

    class rpc_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.rpc_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "rpc_name"
    # proto_parser.g:170:1: rpc_name : IDENTIFIER ;
    def rpc_name(self, ):

        retval = self.rpc_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER116 = None

        IDENTIFIER116_tree = None

        try:
            try:
                # proto_parser.g:170:10: ( IDENTIFIER )
                # proto_parser.g:170:12: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                IDENTIFIER116=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_rpc_name1091)

                IDENTIFIER116_tree = self._adaptor.createWithPayload(IDENTIFIER116)
                self._adaptor.addChild(root_0, IDENTIFIER116_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "rpc_name"

    class req_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.req_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "req_name"
    # proto_parser.g:171:1: req_name : all_identifier ;
    def req_name(self, ):

        retval = self.req_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        all_identifier117 = None



        try:
            try:
                # proto_parser.g:171:10: ( all_identifier )
                # proto_parser.g:171:12: all_identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_all_identifier_in_req_name1099)
                all_identifier117 = self.all_identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, all_identifier117.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "req_name"

    class resp_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(proto_parser.resp_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "resp_name"
    # proto_parser.g:172:1: resp_name : all_identifier ;
    def resp_name(self, ):

        retval = self.resp_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        all_identifier118 = None



        try:
            try:
                # proto_parser.g:172:11: ( all_identifier )
                # proto_parser.g:172:13: all_identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_all_identifier_in_resp_name1107)
                all_identifier118 = self.all_identifier()

                self._state.following.pop()
                self._adaptor.addChild(root_0, all_identifier118.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "resp_name"


    # Delegated rules


 

    FOLLOW_set_in_all_identifier0 = frozenset([1])
    FOLLOW_IDENTIFIER_in_all_value129 = frozenset([1])
    FOLLOW_literal_value_in_all_value136 = frozenset([1])
    FOLLOW_set_in_literal_value0 = frozenset([1])
    FOLLOW_PROTOBUF_TYPE_LITERAL_in_proto_type185 = frozenset([1])
    FOLLOW_all_identifier_in_proto_type192 = frozenset([1])
    FOLLOW_package_def_in_proto208 = frozenset([7, 8, 9, 10, 11, 12, 16])
    FOLLOW_import_def_in_proto212 = frozenset([7, 8, 9, 10, 11, 12, 16])
    FOLLOW_option_line_def_in_proto216 = frozenset([7, 8, 9, 10, 11, 12, 16])
    FOLLOW_enum_def_in_proto220 = frozenset([7, 8, 9, 10, 11, 12, 16])
    FOLLOW_ext_def_in_proto224 = frozenset([7, 8, 9, 10, 11, 12, 16])
    FOLLOW_message_def_in_proto228 = frozenset([7, 8, 9, 10, 11, 12, 16])
    FOLLOW_service_def_in_proto232 = frozenset([7, 8, 9, 10, 11, 12, 16])
    FOLLOW_EOF_in_proto236 = frozenset([1])
    FOLLOW_PACKAGE_LITERAL_in_package_def286 = frozenset([62, 63])
    FOLLOW_package_name_in_package_def288 = frozenset([28])
    FOLLOW_ITEM_TERMINATOR_in_package_def290 = frozenset([1])
    FOLLOW_all_identifier_in_package_name314 = frozenset([1])
    FOLLOW_IMPORT_LITERAL_in_import_def328 = frozenset([55])
    FOLLOW_import_file_name_in_import_def330 = frozenset([28])
    FOLLOW_ITEM_TERMINATOR_in_import_def332 = frozenset([1])
    FOLLOW_STRING_LITERAL_in_import_file_name356 = frozenset([1])
    FOLLOW_OPTION_LITERAL_in_option_line_def370 = frozenset([21, 62])
    FOLLOW_option_name_in_option_line_def372 = frozenset([25])
    FOLLOW_EQUALS_in_option_line_def374 = frozenset([19, 52, 55, 59, 61, 62])
    FOLLOW_option_all_value_in_option_line_def376 = frozenset([28])
    FOLLOW_ITEM_TERMINATOR_in_option_line_def378 = frozenset([1])
    FOLLOW_BRACKET_OPEN_in_option_field_def407 = frozenset([21, 62])
    FOLLOW_option_field_item_in_option_field_def410 = frozenset([24, 27])
    FOLLOW_COMMA_in_option_field_def413 = frozenset([21, 62])
    FOLLOW_option_field_item_in_option_field_def416 = frozenset([24, 27])
    FOLLOW_BRACKET_CLOSE_in_option_field_def420 = frozenset([1])
    FOLLOW_option_name_in_option_field_item435 = frozenset([25])
    FOLLOW_EQUALS_in_option_field_item437 = frozenset([19, 52, 55, 59, 61, 62])
    FOLLOW_option_all_value_in_option_field_item439 = frozenset([1])
    FOLLOW_all_value_in_option_all_value467 = frozenset([1])
    FOLLOW_option_value_object_in_option_all_value473 = frozenset([1])
    FOLLOW_BLOCK_OPEN_in_option_value_object487 = frozenset([20, 62])
    FOLLOW_option_value_item_in_option_value_object489 = frozenset([20, 62])
    FOLLOW_BLOCK_CLOSE_in_option_value_object492 = frozenset([1])
    FOLLOW_IDENTIFIER_in_option_value_item520 = frozenset([26])
    FOLLOW_COLON_in_option_value_item522 = frozenset([19, 52, 55, 59, 61, 62])
    FOLLOW_option_all_value_in_option_value_item524 = frozenset([1])
    FOLLOW_IDENTIFIER_in_option_name553 = frozenset([1])
    FOLLOW_PAREN_OPEN_in_option_name573 = frozenset([62, 63])
    FOLLOW_all_identifier_in_option_name575 = frozenset([22])
    FOLLOW_PAREN_CLOSE_in_option_name577 = frozenset([1, 64])
    FOLLOW_FIELD_IDENTIFIER_in_option_name579 = frozenset([1, 64])
    FOLLOW_ENUM_LITERAL_in_enum_def612 = frozenset([62])
    FOLLOW_enum_name_in_enum_def614 = frozenset([19])
    FOLLOW_BLOCK_OPEN_in_enum_def616 = frozenset([9, 20, 62])
    FOLLOW_enum_content_in_enum_def618 = frozenset([20])
    FOLLOW_BLOCK_CLOSE_in_enum_def620 = frozenset([1])
    FOLLOW_IDENTIFIER_in_enum_name646 = frozenset([1])
    FOLLOW_option_line_def_in_enum_content656 = frozenset([1, 9, 62])
    FOLLOW_enum_item_def_in_enum_content660 = frozenset([1, 9, 62])
    FOLLOW_IDENTIFIER_in_enum_item_def674 = frozenset([25])
    FOLLOW_EQUALS_in_enum_item_def676 = frozenset([52])
    FOLLOW_INTEGER_LITERAL_in_enum_item_def678 = frozenset([23, 28])
    FOLLOW_option_field_def_in_enum_item_def680 = frozenset([28])
    FOLLOW_ITEM_TERMINATOR_in_enum_item_def683 = frozenset([1])
    FOLLOW_MESSAGE_LITERAL_in_message_def717 = frozenset([62])
    FOLLOW_message_name_in_message_def719 = frozenset([19])
    FOLLOW_BLOCK_OPEN_in_message_def721 = frozenset([9, 10, 11, 13, 20, 32])
    FOLLOW_message_content_in_message_def723 = frozenset([20])
    FOLLOW_BLOCK_CLOSE_in_message_def726 = frozenset([1])
    FOLLOW_IDENTIFIER_in_message_name753 = frozenset([1])
    FOLLOW_option_line_def_in_message_content763 = frozenset([1, 9, 10, 11, 13, 32])
    FOLLOW_message_item_def_in_message_content767 = frozenset([1, 9, 10, 11, 13, 32])
    FOLLOW_message_def_in_message_content771 = frozenset([1, 9, 10, 11, 13, 32])
    FOLLOW_enum_def_in_message_content775 = frozenset([1, 9, 10, 11, 13, 32])
    FOLLOW_message_ext_def_in_message_content779 = frozenset([1, 9, 10, 11, 13, 32])
    FOLLOW_PROTOBUF_SCOPE_LITERAL_in_message_item_def792 = frozenset([48, 62, 63])
    FOLLOW_proto_type_in_message_item_def794 = frozenset([62])
    FOLLOW_IDENTIFIER_in_message_item_def796 = frozenset([25])
    FOLLOW_EQUALS_in_message_item_def798 = frozenset([52])
    FOLLOW_INTEGER_LITERAL_in_message_item_def800 = frozenset([23, 28])
    FOLLOW_option_field_def_in_message_item_def802 = frozenset([28])
    FOLLOW_ITEM_TERMINATOR_in_message_item_def805 = frozenset([1])
    FOLLOW_EXTENSIONS_DEF_LITERAL_in_message_ext_def840 = frozenset([52])
    FOLLOW_INTEGER_LITERAL_in_message_ext_def842 = frozenset([14])
    FOLLOW_EXTENSIONS_TO_LITERAL_in_message_ext_def844 = frozenset([15, 52])
    FOLLOW_INTEGER_LITERAL_in_message_ext_def849 = frozenset([28])
    FOLLOW_EXTENSIONS_MAX_LITERAL_in_message_ext_def855 = frozenset([28])
    FOLLOW_ITEM_TERMINATOR_in_message_ext_def858 = frozenset([1])
    FOLLOW_EXTEND_LITERAL_in_ext_def889 = frozenset([62, 63])
    FOLLOW_ext_name_in_ext_def891 = frozenset([19])
    FOLLOW_BLOCK_OPEN_in_ext_def893 = frozenset([9, 10, 11, 20, 32])
    FOLLOW_ext_content_in_ext_def895 = frozenset([20])
    FOLLOW_BLOCK_CLOSE_in_ext_def898 = frozenset([1])
    FOLLOW_all_identifier_in_ext_name925 = frozenset([1])
    FOLLOW_option_line_def_in_ext_content935 = frozenset([1, 9, 10, 11, 32])
    FOLLOW_message_item_def_in_ext_content939 = frozenset([1, 9, 10, 11, 32])
    FOLLOW_message_def_in_ext_content943 = frozenset([1, 9, 10, 11, 32])
    FOLLOW_enum_def_in_ext_content947 = frozenset([1, 9, 10, 11, 32])
    FOLLOW_SERVICE_LITERAL_in_service_def963 = frozenset([62])
    FOLLOW_service_name_in_service_def965 = frozenset([19])
    FOLLOW_BLOCK_OPEN_in_service_def967 = frozenset([9, 18, 20])
    FOLLOW_service_content_in_service_def969 = frozenset([20])
    FOLLOW_BLOCK_CLOSE_in_service_def972 = frozenset([1])
    FOLLOW_IDENTIFIER_in_service_name999 = frozenset([1])
    FOLLOW_option_line_def_in_service_content1009 = frozenset([1, 9, 18])
    FOLLOW_rpc_def_in_service_content1013 = frozenset([1, 9, 18])
    FOLLOW_RPC_LITERAL_in_rpc_def1028 = frozenset([62])
    FOLLOW_rpc_name_in_rpc_def1030 = frozenset([21])
    FOLLOW_PAREN_OPEN_in_rpc_def1032 = frozenset([62, 63])
    FOLLOW_req_name_in_rpc_def1034 = frozenset([22])
    FOLLOW_PAREN_CLOSE_in_rpc_def1036 = frozenset([17])
    FOLLOW_RETURNS_LITERAL_in_rpc_def1038 = frozenset([21])
    FOLLOW_PAREN_OPEN_in_rpc_def1040 = frozenset([62, 63])
    FOLLOW_resp_name_in_rpc_def1042 = frozenset([22])
    FOLLOW_PAREN_CLOSE_in_rpc_def1044 = frozenset([19, 28])
    FOLLOW_BLOCK_OPEN_in_rpc_def1047 = frozenset([9, 20])
    FOLLOW_option_line_def_in_rpc_def1049 = frozenset([9, 20])
    FOLLOW_BLOCK_CLOSE_in_rpc_def1052 = frozenset([1, 28])
    FOLLOW_ITEM_TERMINATOR_in_rpc_def1054 = frozenset([1])
    FOLLOW_ITEM_TERMINATOR_in_rpc_def1059 = frozenset([1])
    FOLLOW_IDENTIFIER_in_rpc_name1091 = frozenset([1])
    FOLLOW_all_identifier_in_req_name1099 = frozenset([1])
    FOLLOW_all_identifier_in_resp_name1107 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("proto_parserLexer", proto_parser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
